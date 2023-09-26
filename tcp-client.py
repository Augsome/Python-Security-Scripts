import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET indicates using standard IPv4, SOCK_STREAM indicates using TCP Client

# Connect the client
client.connect((target_host,target_port))

# Send some data as bytes
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print(response.decode())
client.close()

# Code makes

'''
Code snippet makes some serious assumptions about sockets.

1st assumes that our connection will always succeed.
2nd is that the server expects us to send data first (sometimes the server sends first and awaits a client response.)
3rd is that the server will always return data in a timely fashion.
 '''


