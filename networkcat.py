import argparse
import socket
import shlex
import subprocess # Powerful process-creation interface to interact with client programs
import sys
import textwrap
import threading

# Function receives a command, runs it, and returns output as a string.
def execute(cmd):
	cmd = cmd.strip()
	if not cmd:
		return

	output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT) # check_output() runs a command on local OS and returns ouput from command.
	return output.decode()

# Function if program runs as a sender
def send(self):
	self.socket.connect((self.args.target, self.args.port)) # Conenct to target and port
	if self.buffer:
		self.socket.send(self.buffer)

	try: # Try/except block so we can manually close connection with 'CTRL+C'
		while True: # Loop to receive data from the target
			recv_len = 1 
			response = ''
			while recv_len:
				data = self.socket.recv(4096)
				recv_len = len(data)
				response += data.decode()
				if recv_len < 4096:
					break # If no more data, break loop
			if response:
				print(response)
				buffer = input('> ')
				buffer += '\n'

				self.socket.send(buffer.encode()) # Otherwise, we print the response data and pause for interactive input, and send the input and continue the loop.

	except KeyBoardInterrupt: # Loop continues until keyboard interrupt occurs.
		print('User terminated.')
		self.socket.close()
		sys.exit()

# Function if program runs as a listener
def listen(self):
	self.socket.bind((self.args.target, self.args.port)) # Binds to target and port
	self.socket.listen(5)

	while True: # Starts listening in a loop
		client_socket, _ = self.socket.accept()
		client_thread = threading.Thread(target=self.handle, args=(client_socket,)) # Passing connected socket to handle method
		client_thread.start()

# Logic to perform file uploads, execute commands, and create an interactive shell.
# handle() executes tasks corresponding to the command line argument it receives.
def handle(self, client_socket): 
	if self.args.execute: # Pass cmd to execute() and sends output back to socket
		output = execute(self.args.execute)
		client_socket.send(output.encode())

	elif self.args.upload: # Setup loop to listen on listening socket and receive data until no more is coming in, then write content to the specified file.
		file_buffer = b''
		while True:
			data = client_socket.recv(4096)
			if data:
				file_buffer += data
			else:
				break

		with open(self.args.upload, 'wb') as f:
			f.write(file_buffer)
		message = f'Saved file {self.args.upload}'
		client_socket.send(message.encode())

	elif self.args.command: # Set up a loop, prompt the sender, wait for command string to come back and execute the function.
		cmd_buffer = b''
		while True:
			try:
				client_socket.send(b'BHP: #> ')
				while '\n' not in cmd_buffer.decode():
					cmd_buffer += client_socket.recv(64)
				response = execute(cmd_buffer.decode())
				if response:
					client_socket.send(response.encode())
				cmd_buffer = b''
			except Exception as e:
				print(f'server killed {e}')
				self.socket.close()
				sys.exit()

class NetCat:
	def __init__(self, args, buffer=None): # Initialize NetCat object with command line args and buffer
		self.args = args 
		self.buffer = buffer

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the socket
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	def run(self): # Entry point for managing NetCat object; either setup listener, otherwise call send
		if self.args.listen:
			self.listen()
		else:
			self.send()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='BHP Net Tool', formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent('''Example: netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell 
		netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to a file 
		netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command 
		echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135 
		netcat.py -t 192.168.1.108 -p 5555 # connect to server'''))
	parser.add_argument('-c', '--command', action='store_true', help='command shell')
	parser.add_argument('-e', '--execute', help='execute specified command')
	parser.add_argument('-l', '--listen', action='store_true', help='listen')
	parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
	parser.add_argument('-t', '--target', default='192.168.1.203', help='specified IP')
	parser.add_argument('-u', '--upload', help='upload file')
	args = parser.parse_args()

	'''
	Use argparse module to create a command line interface.
	Six arguments to specify how we want the progrram to behave.
	-c sets interactive shell
	-e executes one specific command
	-l indicates that a listener should be setup
	-p specifies communication port
	-t specifies target IP
	-u name of file to upload

	Both senders and receivers can utilize the program so arguments define whether its invoked to send or listen.

	The -c, -e, and -u arguments imply the -l argument as they apply to listener side.
	The -t and -p arguments define the target listener.
	'''
	if args.listen:
		buffer = '' # If listener, invoke NetCat object with empty buffer
	else:
		buffer = sys.stdin.read() # Otherwise, send the buffer content from STDIN

	nc = NetCat(args, buffer.encode())
