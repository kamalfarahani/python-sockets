import socket
import threading
import constants

from typing import List, Tuple

ClientData = Tuple[socket.socket, str]


class Server:
    def __init__(self, ip: str, port: int) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen()
        self.clients: List[ClientData] = []
    
    def broadcast(self, msg: str) -> None:
        for client_socket, _ in self.clients:
            client_socket.send(msg.encode(constants.ENCODING))

    def recieve_message(self, client_data: ClientData):
        client_socket, client_name = client_data
        while True:
            try:
                msg = client_socket.recv(constants.BYTE_SIZE).decode(constants.ENCODING)
                if len(msg) == 0:
                    raise Exception()
                broadcast_msg = f'{client_name}: {msg}'
                self.broadcast(broadcast_msg)
            except:
                self.clients.remove(client_data)
                client_socket.close()
                self.broadcast(f'{client_name}: {constants.LEFT_TEXT}')
                break

    def connect_client(self):
        while True:
            client_socket, _ = self.socket.accept()
            client_name = client_socket.recv(constants.BYTE_SIZE).decode(constants.ENCODING)
            client_data = (client_socket, client_name)
            self.clients.append(client_data)
            self.broadcast(f'{client_name} {constants.JOINED_MSG}')
            recieve_thread = threading.Thread(target=self.recieve_message, args=(client_data,))
            recieve_thread.start()

    def run(self):
        connect_thread = threading.Thread(target=self.connect_client)
        connect_thread.start()

def main():
    server = Server(constants.SERVER_IP, constants.SERVER_PORT)
    server.run()

if __name__ == '__main__':
    main()