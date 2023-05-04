import socket


LISTENING_PORT = 3333
SERVER_IP = socket.gethostbyname(socket.gethostname())
ENCODING= 'utf-8'
BYTE_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, LISTENING_PORT))
server_socket.listen()
print(f'Listening on port {LISTENING_PORT}')

client_socket, client_addr = server_socket.accept()
client_socket.send('You are connected!'.encode(ENCODING))

while True:
    msg = client_socket.recv(BYTE_SIZE).decode(ENCODING)
    if msg == 'quit':
        client_socket.send('quit'.encode(ENCODING))
        print('Ending chat...')
        break

    print(msg)
    back_msg = input('Enter message: ')
    client_socket.send(back_msg.encode(ENCODING))

server_socket.close()