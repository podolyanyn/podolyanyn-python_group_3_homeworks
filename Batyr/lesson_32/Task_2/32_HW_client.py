import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8888        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world&30')
    s.sendall(f'{input('Pls enter text: ')}&{int(input('Pls enter integer number: '))}'.encode())
    data = s.recv(1024)

print('Received', repr(data.decode()))