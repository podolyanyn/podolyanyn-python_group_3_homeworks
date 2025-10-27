import socket
import threading

stop_event = threading.Event()

def conn_proc(connect, address):
    with connect:
        print('Connected by', address)
        try:
            data = connect.recv(1024).decode('UTF-8')
            print('Received data:', data)

            if data == 'stop_server':
                stop_event.set()
                connect.sendall('Stopping server...'.encode('UTF-8'))

            elif data:
                text = data.upper()
                connect.sendall(text.encode('UTF-8'))
                print(f'Send data: {text}')

        except Exception as e:
            print(f"Connection error: {e}")


if __name__ == '__main__':

    HOST = '127.0.0.1'  # Адрес сервера
    PORT = 65432  # Порт

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(5)
        sock.settimeout(1.0)

        print('Waiting for connection...')

        while not stop_event.is_set():
            try:
                connect, address = sock.accept()
                t = threading.Thread(target=conn_proc, args=(connect, address))
                t.start()
            except socket.timeout:
                continue
            except Exception as e:
                if stop_event.is_set():
                    break
                print(f"Error accept: {e}")
        print('Server stopped.')