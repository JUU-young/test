import socket
import struct

#클라이언트 설정
host = "192.168.0.4"
port = 1212
# 전달해야할 데이터
bo, b1, b2, n, b3 = 1, 1, 1, 17, 0
value = 3.14

packet = struct.pack("!BBBBBf", bo, b1, b2, n, b3, value)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

client_socket.sendall(packet)


data = client_socket.recv(1024)
msg = data.decode('utf-8')
print('echo msg', msg)

client_socket.close()