#!/bin/python3


import sys
import socket
import datetime

# Conditional to check for 2 arguments
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax: python3 PortScanner.py {IP address}")
    sys.exit()

# Input banner
print()
print("-" * 50)
print("Scanning {}".format(target))
print("Start: " + str(datetime.datetime.now().replace(microsecond = 0)))
print("-" * 50)
print()

# Number of the ports that are open in the range
numOpenPorts = 0

# Lower and upper bound of the ports to be scanned
lowerBound = int(input("Enter the lowest port to scan: "))
upperBound = int(input("Enter the highest port to scan: "))
print()

# Loop through specified ports and return results
try:
    for port in range(lowerBound, upperBound + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.25)
        result = s.connect_ex((target, port))
        if (result == 0):
            print("Port {} is open".format(port))
            numOpenPorts = numOpenPorts + 1
            s.close()
except KeyboardInterrupt:
        print()
        print("Exiting program.")
        sys.exit()
except socket.gaierror:
    print()
    print("Host name could not be resolved.")
    sys.exit()
except socket.error:
    print()
    print("Couldn't connect to host")
    sys.exit()

# Output banner
print()
print("-" * 50)
print("End: " + str(datetime.datetime.now().replace(microsecond = 0)))
print("There are {} ports open from port {} to port {}".format(numOpenPorts, lowerBound, upperBound))
print("-" * 50)
print()