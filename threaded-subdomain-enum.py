#Threaded Subdomain Enumeration Script

import requests, sys, threading

def check_subdomain(subdomain, target_domain):
	sub_domain_url = f"http://{subdomain}.{target_domain}"
	try:
		response = requests.get(sub_domain_url)
		if response.status_code == 200:
			print("Valid subdomain: ",sub_domain_url)
		except requests.ConnectionError:
			pass

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 threaded-subdomain-enum.py <target_domain")
		sys.exit(1)

	target_domain = sys.argv[1]

#Read subdomains from a file
with open("subdomains.txt") as file:
	subdomains = file.read().splitlines()