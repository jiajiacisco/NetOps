# Model-Driven Telemetry (MDT)

**Background:** Explore using IaC to provision resources on the Cloud and logging of network telemetry data from network devices for resource management 
<br/>

**Project Components:** 
1. **Terraform** Spin up C8000V Virtual Router on AWS
2. **Python** Establish dial-in MDT subscription using NETCONF with the Virtual Router and redirect telemetry data to logstash
3. **ELK** Store, process and display data in graphical visualisations. ELK uses an open-source container [image](https://github.com/deviantony/docker-elk)
   
**Project Images**<br />

1. **AWS Instances:** Run `terraform apply` to spin up C8000V router on AWS Console
![App Interface Diagram](https://github.com/jiajiacisco/NetOps/blob/main/MDT/images/c.png)

2. **Telemetry Data:** Run `python3 telemetry.py` to start streaming the telemetry data to ELK Stack
![App Interface Diagram](https://github.com/jiajiacisco/NetOps/blob/main/MDT/images/b.png)

3. **ELK DashBoard:** Visualise the output in a console
![App Interface Diagram](https://github.com/jiajiacisco/NetOps/blob/main/MDT/images/d.png)

# Overview <br />
![Overall Block Diagram](https://github.com/jiajiacisco/NetOps/blob/main/MDT/images/a.png)

**Technolgies Used:** 
Terraform, Python, AWS, NETCONF and ELK



