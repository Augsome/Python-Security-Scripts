# Simple Port Scanning Script

'''
Script aiming to build a simple port scanner.
Also, added an ascii banner cause why not??
'''

import sys
import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Augsome's \n Python \n Port Scanner!")
print(ascii_banner)

ip = '192.168.1.6'
open_ports = []

ports = range(1, 65535)

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

for port in ports:
	sys.stdout.flush()
	response = probe_port(ip, port)
	if response == 0:
		open_ports.append(port)

if open_ports:
	print("The open ports are: ")
	print(sorted(open_ports))
else:
	print("It looks like there are no open ports :/")