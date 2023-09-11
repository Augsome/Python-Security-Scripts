# Network Scanner Script

''' 
Simple ARP broadcast scanner utilizing Scapy.
'''

from scapy.all import *

interface = "eth0" #Local Network Interface
ip_range = "10.10.X.X/24" #Local subnet to scan
broadcastMac = "ff:ff:ff:ff:ff:ff" # Broadcast MAC addy

packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout = 2, iface=interface, inter = 0.1)

for send,receive in ans:
	print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))

