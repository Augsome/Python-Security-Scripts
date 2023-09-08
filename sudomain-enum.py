# Subdomain Enumeration Script

''' 
Finding subdomains used by the target organization is an effective way to increase the attack surface and discover more vulnerabilities.
This script will use a list of potential subdomains and prepends them to the domain name provided via a command-line argument.
The script then tries to connect the subdomains and assumes the ones that accept the connection exist.
'''

import requests #Library to make HTTP GET Requests
import sys #Library for accepting command-line arguments

sub_list = open("subdomains.txt").read() #Reading from subdomain list file
sub_doms = sub_list.splitlines() #Parsing out subdomain values individually

for sub in sub_doms:
	sub_domains = f"http://{sub}.{sys.argv[1]}" #Loop for prepending subdomains to target domain GET requests
	try:
		requests.get(sub_domains)

	except requests.ConnectionError: #Error for non-valid subdomains
		pass

	else:
		print("Valid domain: ", sub_domains) #Successful subdomain discovery