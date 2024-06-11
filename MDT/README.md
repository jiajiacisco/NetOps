# Model-Driven Telemetry (MDT)

**Background:** Explore using IaC to provision resources on the Cloud and logging of network telemetry data from network devices for resource management 
<br/>

**Project Components:** 
1. **Terraform** Spin up C800V Virtual Router on AWS
2. **Python** Establish dial-in MDT subscription using NETCONF with the Virtual Router and redirect telemetry data to logstash
3. **ELK** Store, process and display data in graphical visualisations. ELK uses an open-source container [image](https://github.com/deviantony/docker-elk)
   
**Product Overview**<br />
1. **Login Page** Enter your Meraki API Key that is obtainable from your Meraki Dashboard
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/blob/main/images/p3.png)
3. **Query Page** The webpage will fetch the Meraki Organisation and Network your API Key has access to. Select what you wish to query and input the datetime period too
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p4.png)
4. **Query Records Page** Display data for all users that associated and disassociate with the Meraki Network. Data is downloadable into excel for further use
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p5.png)
5. **Built-in Search Functionality** Allow users to search and filter data for a particular date, User Name or Device Name 
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p6.png)

# Overview <br />
![Overall Block Diagram](https://github.com/jiajiacisco/NetOps/MDT/tree/main/images/a.png)


**Technolgies Used:** 
Terraform, Python, AWS, NETCONF and ELK



