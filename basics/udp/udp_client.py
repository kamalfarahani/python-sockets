import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3333

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto('Hi There!'.encode(), (SERVER_IP, SERVER_PORT))