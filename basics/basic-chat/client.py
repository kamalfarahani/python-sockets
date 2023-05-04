import socket

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3333
ENCODING = 'utf-8'
BYTE_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

while True:
    msg = client_socket.recv(BYTE_SIZE).decode(ENCODING)
    if msg == 'quit':
        client_socket.send('quit'.encode(ENCODING))
        print('Ending chat...')
        break
    
    print(msg)
    back_msg = input('Enter msg: ')
    client_socket.send(back_msg.encode(ENCODING))

client_socket.close()