#!/usr/bin/env python

"""
Purpose: Using NETCONF with operational state YANG models to enable
streaming telemetry to the Elastic (formerly ELK) stack in Docker.
This is an example of dial-in model-driven telemetry (MDT).
"""

import logging
from logstash import TCPLogstashHandler
from ncclient import manager
from lxml.etree import fromstring
import xmltodict


def main():

    # Define basic logging parameters. This script writes JSON-formattet
    # directly to logstash
    logger = logging.getLogger("netconf_mdt")
    logger.setLevel(logging.INFO)

    # Define logstash connection parameters to reach the ELK stack container.
    logstash_params = {"host": "127.0.0.1", "port": 50000, "version": 1}
    logger.addHandler(TCPLogstashHandler(**logstash_params))

    # Define NETCONF connection parameters to reach the Cisco always-on IOS-XE
    netconf_params = {
        "host": "your_aws_public_ip",
        "port": 830,
        "username": "user_password",
        "password": "your_password",
        "hostkey_verify": False,
        "allow_agent": False,
        "look_for_keys": False,
        "device_params": {"name": "iosxe"},
    }

    # Connect to the device and disconnect when scope ends
    with manager.connect(**netconf_params) as conn:

         #Add YANG-based xpath filters to this list to subscribe to multiple
         #topics. Be sure to check the proper YANG model for your version!
        xpaths_desired = [
            "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds",
            "/memory-ios-xe-oper:memory-statistics/memory-statistic",
        ]
        #For every xpath in which to subscribe ...
        for xpath in xpaths_desired:

            # Issue the establish-subscription RPC via helper function
            sub_resp = telemetry_subscribe(conn, xpath)


            # Convert the RPC-reply to a Python dict
            sub_json = xmltodict.parse(sub_resp.xml)
            sub_result = sub_json["rpc-reply"]["subscription-result"]["#text"]


            # Ensure RPC succeeded by checking the 'subscription-result' key
            if "ok" in sub_result.lower():
                # Success text: "notif-bis:ok". Print subscription ID also
                sub_id = sub_json["rpc-reply"]["subscription-id"]["#text"]
                print(f"Subscribed to '{xpath}' via ID: {sub_id}")
            else:
                print(f"Could not subscribe to '{xpath}'. Reason: {sub_result}")

        while True:

            # This blocks until a notification is received
            msg_xml = conn.take_notification()


            # Convert XML for logstash
            msg_json = xmltodict.parse(
                msg_xml.notification_xml, postprocessor=str_to_int
            )

            # Send an INFO log to logstash carrying MDT dict as extra data.
            sub_id = msg_json["notification"]["push-update"]["subscription-id"]
            logger.info(sub_id, extra=msg_json)

            # Print message indicating a notification logged
            timestamp = msg_json["notification"]["eventTime"]
            print(f"Logged update from ID {sub_id} at {timestamp}")



def str_to_int(path, key, value):
    """
    Helper function that automatically converts all strings to
    integers, assuming it is possible.
    This is avoid complex data preprocessing at the elk
    """
    try:
        return (key, int(value))
    except (ValueError, TypeError):
        return (key, value)


def telemetry_subscribe(conn, xpath, period=1000):
    """
    Helper function to subscribe to periodic telemetry events. Issues
    the 'establish-subscription' RPC with the specified xpath and period.
    """

    # yang-ietf paths
    xmlns = "urn:ietf:params:xml:ns:yang:ietf-event-notifications"
    xmlns_yp = "urn:ietf:params:xml:ns:yang:ietf-yang-push"

    # Build RPC text by substiting XML and xpath variables
    subscribe_rpc = f"""
        <establish-subscription xmlns="{xmlns}" xmlns:yp="{xmlns_yp}">
            <stream>yp:yang-push</stream>
            <yp:xpath-filter>{xpath}</yp:xpath-filter>
            <yp:period>{period}</yp:period>
        </establish-subscription>
    """

    subscribe_resp = conn.dispatch(fromstring(subscribe_rpc))
    return subscribe_resp


if __name__ == "__main__":
    main()
