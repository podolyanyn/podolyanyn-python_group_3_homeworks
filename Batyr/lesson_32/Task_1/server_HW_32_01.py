import socket

HOST = 'localhost'
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (HOST, PORT)
print('starting up --- UDP SERVER--- on {} port {}'.format(*server_address))
server.bind(server_address)

while True:
    data, addr = server.recvfrom(1024)  # отримуємо дані та адресу клієнта
    print('Received from', addr, data.decode())
    server.sendto(data.upper(), addr)  # відправляємо назад