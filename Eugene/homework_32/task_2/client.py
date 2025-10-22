import socket

HOST = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

key = 3
message = "Hello, server!"

to_send = f"{key}|{message}".encode()
client_socket.sendto(to_send, (HOST, PORT))

data, addr = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()