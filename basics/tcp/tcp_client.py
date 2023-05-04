import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3333
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

msg = client_socket.recv(1024)
print(msg)
client_socket.close()