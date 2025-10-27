import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

print_lock = threading.Lock()

def conn_proc(mess):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(mess.encode('UTF-8'))
            with print_lock:
                print("Sent by:", mess)
            result_data = sock.recv(1024).decode('UTF-8')
            print('Received:', result_data)
    except Exception as e:
        print(f"Error in thread for '{mess}': {e}")

if __name__ == '__main__':

    list_message = ['First message', 'Second message', 'Third message', 'Fourth message', 'Fifth message']

    list_threads = []

    for message in list_message:
        t = threading.Thread(target=conn_proc, args=(message,))
        list_threads.append(t)
        t.start()

    for t in list_threads:
        t.join()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall('stop_server'.encode('UTF-8'))
            print('A command has been sent to stop the server...')
            data = s.recv(1024).decode('UTF-8')
            print('Received:', data)
    except Exception as e:
        print(f"Stop error: {e}")