import socket
import multiprocessing

def handle_connection(connect, address):

    print(f"Client from adress: {address}")
    try:
        while True:
            data = connect.recv(1024)
            if not data:
                break
            connect.sendall(data)
            print(f"Echo: {data.decode('utf-8', errors='ignore').strip()}")
    except Exception as e:
        print(f"Error from {address}: {e}")
    finally:
        connect.close()
        print(f"Client {address} disconnected")


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server on {HOST}:{PORT}. Listen.")

    while True:
        client_socket, address = server_socket.accept()
        process = multiprocessing.Process(target=handle_connection, args=(client_socket, address))
        process.daemon = True
        process.start()
        print(f"Proc for {address} start")