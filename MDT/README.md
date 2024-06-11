# Meraki Student Presence

**Background:** University is looking to refresh exiting network equipment. To position Meraki in a stronger position, we wanted to show that besides providing network connectivity and cloud-based management
Meraki APIs can be used to simplify certain opertional and administrative works in the school environment 
<br/>

**Product Description** <br/>
MerakiStudetPresence makes use of Meraki APIs and telemetry data to enable univerity admins to have greater visbility into a student's activity in the univeristy campus <br/>

**Use Cases:** 
1. **Attendance Taking** Verify if a student visited the campus on a certain date and time
2. **Location Analytics** Verify student location on campus based on the Access Point it connected to
3. **Device Lost&Found** If a device goes missing, we can narrow down the location by checking which access point it is connected to

**Product Overview**<br />
1. **Login Page** Enter your Meraki API Key that is obtainable from your Meraki Dashboard
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/blob/main/images/p3.png)
3. **Query Page** The webpage will fetch the Meraki Organisation and Network your API Key has access to. Select what you wish to query and input the datetime period too
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p4.png)
4. **Query Records Page** Display data for all users that associated and disassociate with the Meraki Network. Data is downloadable into excel for further use
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p5.png)
5. **Built-in Search Functionality** Allow users to search and filter data for a particular date, User Name or Device Name 
![App Interface Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p6.png)

# App Design <br />
![Overall Block Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p1.png)
![Overall Block Diagram](https://github.com/jiajiacisco/MerakiStudentPresence/tree/main/images/p2.png)

**Technolgies Used:** 
Meraki API, ReactJS,Python, Flask




