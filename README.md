# Satellite 6 Perfomance Check

This is a personal project where I'm trying to learn how I can monitor and check the performance of the satellite based on evach componet Red Hat Satellite 6 is using. 

## How to run this script:

1. Download the python script to a system where you a sos-report from the satellite server.

2. Setup the system for the script to give beautiful results. 
~~~
$ sudo pip install PrettyTable
~~~

3. Run the script as root user.
~~~
# python perfcheck.py <sosreport-file>
~~~

# Examples
~~~
# python perfcheck.py <sosreport-file>

NOTICE: Sos-report is having Supported Version of Satellite. 

	Memory Statis of System
+--------------------+-----------+
|        Type        | Size (GB) |
+--------------------+-----------+
| Total Memory(RAM): |   94 GB   |
| Used Memory:       |   24 GB   |
| Free Memory:       |   45 GB   |
+--------------------+-----------+

What will you like to see?
 	 1) Summary of Memory Consumption.
 	 2) Highest Memory Consumpustion based on Users.
 	 3) Highest Memory Consumpustion based on Processes.
 	 4) Exit from program 


 What would you like to see?: 1
	 Summary of High Memory Comsumption By Users. 
+----------+-----------------------+
|  Users   | Total Memory Consumed |
+----------+-----------------------+
| mongodb  |         7.0 GB        |
| foreman  |         6.4 GB        |
| postgres | 2.5000000000000004 GB |
|  tomcat  |         2.5 GB        |
|  apache  |         2.1 GB        |
|  puppet  |         1.6 GB        |
|   root   |         1.0 GB        |
| foreman+ |         0.2 GB        |
|  qpidd   |         0.2 GB        |
|   dbus   |         0.0 GB        |
|  chrony  |         0.0 GB        |
| polkitd  |         0.0 GB        |
|   rpc    |         0.0 GB        |
|   nrpe   |         0.0 GB        |
| postfix  |         0.0 GB        |
| signalf+ |         0.0 GB        |
| ansible+ |         0.0 GB        |
|  redis   |         0.0 GB        |
| qdroute+ |         0.0 GB        |
|  squid   |         0.0 GB        |
+----------+-----------------------+

What will you like to see?
 	 1) Summary of Memory Consumption.
 	 2) Highest Memory Consumpustion based on Users.
 	 3) Highest Memory Consumpustion based on Processes.
 	 4) Exit from program 


 What would you like to see?: 2


List of Users -
 1.apache
 2.foreman
 3.mongodb
 4.postgres
 5.puppet
 6.qdroute+
 7.qpidd
 8.redis
 9.root
 10.squid
 11.tomcat

 Enter the user: 2
+---------+----------------------------+---------+
|  Users  | Total Memory Consumed (GB) | Process |
+---------+----------------------------+---------+
| foreman |            1.1             | sidekiq |
| foreman |            1.0             | sidekiq |
| foreman |            0.9             |  puma:  |
| foreman |            0.9             |  puma:  |
| foreman |            0.8             |  puma:  |
+---------+----------------------------+---------+

What will you like to see?
 	 1) Summary of Memory Consumption.
 	 2) Highest Memory Consumpustion based on Users.
 	 3) Highest Memory Consumpustion based on Processes.
 	 4) Exit from program 


 What would you like to see?: 3


List of Processes -
 1.java
 2.sidekiq
 3.celery
 4.httpd
 5.puppet
 6.puma
 7.qpidd
 8.squid
 9.tomcat
 10.postgres


 Enter the Service: 6
+---------+----------------------------+---------------------------------------------+
|  Users  | Total Memory Consumed (GB) |                   Process                   |
+---------+----------------------------+---------------------------------------------+
| foreman |            0.9             |    puma: cluster worker 3: 563 [foreman]    |
| foreman |            0.9             |    puma: cluster worker 2: 563 [foreman]    |
| foreman |            0.8             |    puma: cluster worker 1: 563 [foreman]    |
| foreman |            0.7             |    puma: cluster worker 0: 563 [foreman]    |
| foreman |            0.4             | puma 4.3.6 (tcp://127.0.0.1:3000) [foreman] |
+---------+----------------------------+---------------------------------------------+

~~~
# Limitation 

This script can only show content from the sos-report along with it does not include pasenger information as it is already depricated in the satellite 6.9.


# Contribution

I really hope this helps you as well.
Please let me know via email. 
Also, if you believe this project is valuable for you, feel free to share your feedback via contacts below. This will help me to push this project forward.

Thank you in advance! :)


# Author 

Name: Jaskaran Singh Narula.

Email: narula.jaskaran@gmail.com

Website: www.jaskaran.me 




