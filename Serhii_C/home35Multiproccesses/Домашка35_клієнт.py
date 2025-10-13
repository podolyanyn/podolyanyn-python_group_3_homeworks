import pickle
import socket
import time
text = ('20240123','20250924','eur')
HOST ='localhost'
PORT = 8084

start_time = time.perf_counter()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    tuple_for_send = pickle.dumps(text)

    s.sendall(tuple_for_send)
    data: bytes = s.recv(100000)
    received_data = pickle.loads(data)
print('Received', repr(received_data))
end_time = time.perf_counter()
print(f'Отримання даних виконано за :{end_time - start_time}')