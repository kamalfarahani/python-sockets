import socket


SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3333
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

while True:
    msg, addr = server_socket.recvfrom(1024)
    print(msg.decode('utf-8'))
    print(addr)