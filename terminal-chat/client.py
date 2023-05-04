import socket
import threading
import constants


class Client:
    def __init__(self, name: str, server_ip: str, server_port: int) -> None:
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server_ip, server_port))
        self.socket.send(name.encode(constants.ENCODING))
    
    def send_message(self):
        while True:
            msg = input()
            self.socket.send(msg.encode(constants.ENCODING))

    def recieve_message(self):
        while True:
            try:
                msg = self.socket.recv(constants.BYTE_SIZE).decode(constants.ENCODING)
                print(msg)
            except:
                self.socket.close()
                break
    
    def run(self):
        send_thread = threading.Thread(target=self.send_message)
        recieve_thread = threading.Thread(target=self.recieve_message)

        send_thread.start()
        recieve_thread.start()


def main():
    name = input('Enter name: ')
    client = Client(name, constants.SERVER_IP, constants.SERVER_PORT)
    client.run()


if __name__ == '__main__':
    main()