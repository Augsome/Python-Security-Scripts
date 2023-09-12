# Hash Cracker Script

'''
Script explanation

1. Ask for the location of the wordlist
2. Ask for the MD5 hash to be cracked
3. Reads values from wordlist
4. Converts cleartext values to MD5 hashes
5. Compares the generated MD5 hash value with the value entered by the user

Hashlib allows for building hash crackers according to requirements w/support 
for a wide range of algorithms.

Hash values cannot be cracked as they do not contain the cleartext value.
Cleartext values for hashes can only be found with a list of potential cleartext values.

The script requires two inputs: the location of the wordlist and the hash value.
'''

import hashlib

wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: '))

with open(wordlist_location, 'r') as file:
	for line in file.readlines()
	hash_ob = hashlib.md5(line.strip().encode())
	hashed_pass = hash_ob.hexdigest()
	if hashed_pass == hash_input:
		print('Found cleartext password! ' + line.strip())
		exit(0)