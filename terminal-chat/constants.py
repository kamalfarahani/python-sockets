import socket


SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 3334
ENCODING = 'utf-8'
BYTE_SIZE = 1024
JOINED_MSG = 'Joined!'
LEFT_TEXT = 'left!'
ENTER_MSG_TEXT = '> '