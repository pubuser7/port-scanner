#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServerIP = raw_input("Enter the host for scan: ")

print '-' * 60
print "Pleas wait, scanning remote host", remoteServerIP
print 

t1 = datetime.now()

try:
    for port in range(1, 65535):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerIP, port))
	if result == 0:
	    print "Port %s: Open" %port
	sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()

except socket.error:
	print "Couldn't connect to server"
	sys.exit()

t2 = datetime.now()
total = t2 - t1

print
print "Scanning Completed in: ", total
