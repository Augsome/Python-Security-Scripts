# File Download Script

'''
Wget on Linux Systems or Certutil on Windows are useful tools for downloading files.
Similarly, Python can be used for the same purpose.
'''

import requests

url = 'https://assets.tryhackme.com/img/THMlogo.png'
r = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(r.content)

'''
This code can be easily adapted to retrieve any other type of file

import requests

url = 'https://download.sysinternals.com/files/PSTools.zip'
r = requests.get(url, allow_redirects=True)
open('PSTools.zip', 'wb').write(r.content)
'''