import json
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5001
BUFFER_SIZE = 1024


class TCPCommunication:

    def __init__(self):
        self.tcp_ip = TCP_IP
        self.tcp_port = TCP_PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((TCP_IP, TCP_PORT))

    def is_device_activate(self, data):
        """
        :param data:
        :return:
        """
        self.sock.send(data)
        data = self.sock.recv(BUFFER_SIZE)
        self.sock.close()
        decoded = data.decode('utf-8')
        # json_data = json.loads(data)
        print("Receive data", decoded)
        return decoded
