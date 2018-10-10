import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5001
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)

device = {
    "uuid": "123456"
}

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    data_rcv = data.decode('utf-8')
    check = {"uuid": data_rcv}
    if check.items() <= device.items():
        conn.send(b"{'active': True}")
    print("received data:", data_rcv)
    # conn.send(data)  # echo
conn.close()
