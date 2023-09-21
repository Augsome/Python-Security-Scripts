#Directory Enumeration Script w/Threading Capabilities

import requests
import sys

#Read the wordlist and split it into a list of directories
with open("wordlist.txt") as file:
	directories = file.read().splitlines()

def check_directory(dir):
	dir_enum = f"http://{sys.argv[1]}/{dir}.html"
	r = requests.get(dir_enum)
	if r.status_code == 404:
		pass
	else:
		print("Valid directory: ", dir_enum)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 threaded-dir-enum.py <target>")
		sys.exit(1)

	target = sys.argv[1]

	#Adjust the number of threads as needed
	num_threads = 4 

	#Split the directories into chunks for threading
	directory_chunks = [directories[i:i + len(directories) // num_threads] for i in range(0, len(directories), len(directories) // num_threads)]

	threads = []

	for chunk in directory_chunks:
		thread = threading.Thread(target=lambda x=chunk: [check_directory(dir) for dir in x])
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()

	print('Directory enumeration completed.')


