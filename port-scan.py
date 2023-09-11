# Simple Port Scanning Script

'''
Script aiming to build a simple port scanner.
'''

#Importing Modules for code
import sys
import socket

#Target machine
ip = f"{sys.argv[1]}"
#ip = '192.168.1.6'
#ip = socket.gethostbyname(host) #Example of obtaining IP from domain name target.

#Empty ports array to be populated with detected ports
open_ports = []

#Ports to be probed
ports = range(1, 65535) #Complete range of ports
#ports = {21,22,23,53,80,135,443,445} #Example of probing specific ports

#Function attempting connection to ports
def probe_port(ip, port, result = 1):
	try:
		sock - socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip, port))
		if r == 0:
			result = r 
		sock.close()
	except Exception as e:
		pass
	return result

#Loop to iterate through the specified port list
for port in ports:
	sys.stdout.flush()
	response = probe_port(ip, port)
	if response == 0:
		open_ports.append(port)

#Results of the port probing 
if open_ports:
	print("The open ports are: ")
	print(sorted(open_ports))
else:
	print("It looks like there are no open ports :/")