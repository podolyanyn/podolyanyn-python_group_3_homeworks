import socket
from HW_functions import *

HOST = 'localhost'
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('starting up --- TCP SERVER --- on {} port {}'.format(*server_address))
server.bind(server_address)

server.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = server.accept()

    with connection:
        print('Connected by', client_address)
        while True:
            data = connection.recv(1024)

            if not data:
                break
            values = data.decode().split('&')
            print(values)
            result = encode_with_ceasar(encode_with_ceasar(values[0], int(values[1])))
            print(result)

            connection.sendall(result.encode())