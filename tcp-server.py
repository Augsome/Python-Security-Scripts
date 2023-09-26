import socket
import threading


IP = '0.0.0.0'
PORT = 9998

def main():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((IP, PORT)) # Port and IP for server to listen on
        server.listen(5) # Max backlog of connections set
        print(f'[*] Listening on {IP}:{PORT}')

        # When client connects, receive client socket in client and remote connection
        # Then create a new thread object pointing at handle_client with client socket 
        while True:
                client, address = server.accept()
                print(f'[*] Accepted connection from {address[0]}:{address[1]}')
                client_handler = threading.Thread(target=handle_client, args=(client>
                client_handler.start() # Start thread to handle the client connection

def handle_client(client_socket):
        with client_socket as sock:
                request = sock.recv(1024)
                print(f'[*] Received: {request.decode("utf-8")}')
                sock.send(b'ACK')

if __name__ == '__main__':
        main()
