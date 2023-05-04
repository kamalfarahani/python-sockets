import socket


LISTENING_PORT = 3333
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
my_ip = socket.gethostbyname(socket.gethostname())
server_socket.bind((my_ip, LISTENING_PORT))
server_socket.listen()
print(f'server ip: {my_ip}')

while True:
    client_socket, client_addr = server_socket.accept()
    client_socket.send('You are connected!'.encode())