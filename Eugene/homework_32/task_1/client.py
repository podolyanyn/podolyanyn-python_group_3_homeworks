import socket

HOST = '127.0.0.1'
PORT = 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b"Hello, server!"
client_socket.sendto(message, (HOST, PORT))

data, addr = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()