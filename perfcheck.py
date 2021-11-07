import sys
import os
import re
import math
from prettytable import PrettyTable


#Taking the sos-report as argument
#print (sys.argv)

#Variables
REPORT = sys.argv[1]                    # sos-report
NAME = sys.argv[1] + "/installed-rpms"  # To check satellite version
FREE = sys.argv[1] + "/free"            # To check free space
PS   = sys.argv[1] + "/ps"              # To get info from ps from the sos.

## Checking Satellite Version
found = False
file = open(NAME, "r")
for line in file:
    if re.search("satellite-6.[7-9]", line):
        print("\nNOTICE: Sos-report is having Supported Version of Satellite. ")
        found = True
if found == False:
    print("\n\t\t ERROR: Sos-report does not have Support Version of Satellite.")
    quit()

# Calculate KB into GB
def convert_size(size):
    if size == 0:
       return "0KB"
    gb = (size/1024)/1024
    return "{} {}".format(int(gb), "GB")

# Checking Free space
file = open(FREE, "r")
for line in file:
    line = line.strip().split()
    myTable = PrettyTable(["Type", "Size (GB)" ])
    if line [0] == "Mem:":
        print("\n\tMemory Statis of System")
        myTable.add_row(["Total Memory(RAM):", convert_size(int(line[1])) ])
        myTable.add_row(["Used Memory:      ", convert_size(int(line[2])) ])
        myTable.add_row(["Free Memory:      ", convert_size(int(line[3])) ])
        print(myTable)

## Function1
def mem_calc():
    mem = {}
    file = open(PS, "r")
    for line in file:
        line = line.strip().split()
        if line[0] == "USER":
            pass
        else:
            if line[0] in mem:
                b = float(line[3])
                mem[line[0]] += b
            else:
                b = float(line[3])
                mem[line[0]] = b
    return mem

## Fucntion2
def user_calc(user):
    users = []
    file = open(PS, "r")
    for line in file:
        line = line.strip().split()
        if line[0] == "USER":
            pass
        else:
            if line[0] == user:
                x = (line[0], line[3], line[10])
                users.append(x)
    users.sort(key = lambda x: x[1], reverse=True)
    x = len(users)
    myTable = PrettyTable(["Users", "Total Memory Consumed (GB)", "Process"])
    if x <=5:
        for i in range(0, x):
            myTable.add_row([users[i][0], users[i][1], users[i][2]])
    else:
        for i in range(0, 5):
            myTable.add_row([users[i][0], users[i][1], users[i][2]])
    print(myTable)

## Fucntion3
def process_show(process):
    users = []
    file = open(PS, "r")
    for line in file:
        line = line.strip().split()
        if line[0] == "USER":
            pass
        else:
            if re.search(process, line[10]):
                x = (line[0], line[3], line[10:])
                users.append(x)
    users.sort(key = lambda x: x[1], reverse=True)
    x = len(users)
    myTable = PrettyTable(["Users", "Total Memory Consumed (GB)", "Process"])
    if x <=5:
        for i in range(0, x):
            myTable.add_row([users[i][0], users[i][1], " ".join(users[i][2])])
    else:
        for i in range(0, 5):
            myTable.add_row([users[i][0], users[i][1], " ".join(users[i][2])])
    print(myTable)


while True:
    print ("\nWhat will you like to see?")
    print (" \t 1) Summary of Memory Consumption.")
    print (" \t 2) Highest Memory Consumpustion based on Users.")
    print (" \t 3) Highest Memory Consumpustion based on Processes.")
    print (" \t 4) Exit from program ")

    ## Variables

    USER_INPUT= int(input("\n\n What would you like to see?: "))

    ## Summary of Memory Consumption

    if USER_INPUT == 1:
        mem  = mem_calc()
        print("\t Summary of High Memory Comsumption By Users. ")
        myTable = PrettyTable(["Users", "Total Memory Consumed"])
        for k, v in sorted(mem.items(), key=lambda item: item[1], reverse=True):
            USER_NAME, MEM_VALUE = k, str(v)+" GB"
            myTable.add_row([USER_NAME, MEM_VALUE])
        print(myTable)


    elif USER_INPUT == 2:
        user_map = {
            "1":"apache",
            "2":"foreman",
            "3":"mongodb" ,
            "4":"postgres" ,
            "5":"puppet" ,
            "6":"qdroute+" ,
            "7":"qpidd" ,
            "8":"redis" ,
            "9":"root" ,
            "10":"squid" ,
            "11":"tomcat"
        }
        print("\n\nList of Users -")
        print(" 1.apache\n 2.foreman\n 3.mongodb\n 4.postgres\n 5.puppet\n 6.qdroute+\n 7.qpidd\n 8.redis\n 9.root\n 10.squid\n 11.tomcat")
        USER_INPUT = input("\n Enter the user: ")
        user = user_map[USER_INPUT]
        mem = user_calc(user)

    elif USER_INPUT == 3:
        process_map = {
            "1":"java",
            "2":"sidekiq",
            "3":"celery" ,
            "4":"httpd" ,
            "5":"puppet" ,
            "6":"puma" ,
            "7":"qpidd" ,
            "8":"squid" ,
            "9":"tomcat",
            "10":"postgres"
        }
        print("\n\nList of Processes -")
        print(" 1.java\n 2.sidekiq\n 3.celery\n 4.httpd\n 5.puppet\n 6.puma\n 7.qpidd\n 8.squid\n 9.tomcat\n 10.postgres\n")
        USER_INPUT = input("\n Enter the Service: ")
        process = process_map[USER_INPUT]
        mem = process_show(process)



    elif USER_INPUT == 4:
        break
