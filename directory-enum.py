# Directory Enumeration Script

'''
Once subdomains have been discovered, the next step is to find directories.
The following code is a simple directory enumeration tool.
The script will loop through and passes all returned "404" responses.

Run script: python3 directory-enum.py 192.168.1.1
'''

import requests
import sys

sub_list - open("wordlist.txt").read()
directories = sub_list.splitlines()

for dir in directories:
	dir_enum = f"http://{sys.argv[1]}/{dir}.html"
	r = requests.get(dir_enum)
	if r.status_code == 404:
		pass
	else:
		print("Valid directory:", dir_enum)