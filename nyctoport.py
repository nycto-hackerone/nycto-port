#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import sys
from datetime import datetime

print "███╗   ██╗██╗   ██╗ ██████╗████████╗ ██████╗       ██████╗  ██████╗ ██████╗ ████████╗"
print "████╗  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝"
print "██╔██╗ ██║ ╚████╔╝ ██║        ██║   ██║   ██║█████╗██████╔╝██║   ██║██████╔╝   ██║   "
print "██║╚██╗██║  ╚██╔╝  ██║        ██║   ██║   ██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║   "
print "██║ ╚████║   ██║   ╚██████╗   ██║   ╚██████╔╝      ██║     ╚██████╔╝██║  ██║   ██║   "
print "╚═╝  ╚═══╝   ╚═╝    ╚═════╝   ╚═╝    ╚═════╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   "
                                                                                     

# Ask for input
remoteServer    = raw_input("Enter the Fucking Victim host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please Fucking, wait on remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 999999)

# We also put in some error handling for catching errors

try:
    for port in range(1,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You Fucking Cancled"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be Fucking resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't Fucking Connect To Server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scan Fucking Completed in: ', total

# Printing the information to screen
print 'Scan Fucking Completed in: ', total
