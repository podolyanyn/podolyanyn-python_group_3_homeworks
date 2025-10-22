import socket

HOST = '127.0.0.1'
PORT = 65432
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"The server is running on {HOST}:{PORT}")

while True:
    data, addr = server_socket.recvfrom(1024)

    print(f"Received from {addr}: {data.decode()}")

    response = b"Server responce: " + data
    server_socket.sendto(response, addr)