import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Change socket type to SOCK_DGRAM

# Send some data
client.sendto(b"AAABBBCCC", (target_host,target_port))
# Simply call sendto() passing in the data and the server you want to send to.
# UDP is connectionless, so no connect() beforehand.

# Receive some data
data, addr = client.recvfrom(4096)
# Call recvfrom() to receive the UDP data back.

print(data.decode())
client.close()
