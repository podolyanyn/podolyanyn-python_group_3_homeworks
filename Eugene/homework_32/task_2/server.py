import socket

def caesar_encrypt (message, key):
    low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    up_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ""
    for char in message:
        if char in low_alphabet:
            char_index = low_alphabet.index(char)
            new_index = (char_index + key) % 26
            result += low_alphabet[new_index]
        elif char in up_alphabet:
            char_index = up_alphabet.index(char)
            new_index = (char_index + key) % 26
            result += up_alphabet[new_index]
        else:
            result += char
    return result

HOST = '127.0.0.1'
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))

print(f"The server is running on {HOST}:{PORT}")

while True:
    data, addr = server_socket.recvfrom(1024)

    parts = data.split(b'|')
    if len(parts) == 2:
        key = int(parts[0].decode())
        message = parts[1].decode()
        print(f"Received from {addr}: key={key}, message={message}")

        encrypted = caesar_encrypt(message, key)

        response = encrypted.encode()
        server_socket.sendto(response, addr)
    else:
        print(f"Incorrect format {addr}")