import pickle
import socket
text = ('20250923','20250924','usd')
HOST ='localhost'
PORT = 8082

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    tuple_for_send = pickle.dumps(text)

    s.sendall(tuple_for_send)
    data: bytes = s.recv(120000)
    received_data = pickle.loads(data)
print('Received', repr(received_data))