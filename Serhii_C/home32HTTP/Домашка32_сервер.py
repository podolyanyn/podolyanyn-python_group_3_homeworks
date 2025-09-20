# Завдання 1
# Під час уроку ми створили сервер і клієнт, які використовують протокол TCP/IP для зв'язку через сокети.'
# (' У цьому завданні вам потрібно створити сервер і клієнт, які використовуватимуть протокол користувацьких дейтаграм (UDP) '
 # 'для зв'язку.)

# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('localhost', 8080)
#
# print('start with {} port{}'.format(*server_address))
# sock.bind(server_address)
#
# while True:
#     print('waiting for message')
#     data, client_address = sock.recvfrom(1024)
#
#     if data:
#         sent = sock.sendto(data.upper(), client_address)

# Завдання 2
#
# Розширити echo-сервер, який повертає клієнту дані, зашифровані за допомогою алгоритму шифрування
# Цезаря за допомогою певного ключа, отриманого від клієнта.

def Cezar(text,key):
    text = text.lower()
    text = list(text)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Алфавит продубльовано 2 рази , тому що якщо написаний 1 раз то , при високих значеннях
#ключа (більше 10) іноді (десь 30% випадків) виникає -out of range.Чому , так і не збагнув.
# Прописав алфавіт 2 рази - все працює.

    try:
        for i in range(len(text)):
            if text[i] in alphabet:
                current_number = alphabet.index(text[i])
                if current_number + key>len(alphabet):
                    new_number = (current_number+key)-(len(alphabet))

                else:
                    new_number = (current_number+key)
                text[i] = alphabet[new_number]
            else:
                text[i] = text[i]
        text = ''.join(text)
    except ValueError:
        pass
    return text


print(Cezar('London is the capital  ',3))

import pickle
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
print ('start with {} port{}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ('connection from', client_address)
        while True:
            data = connection.recv(1024)
            try:
                received_tuple = pickle.loads(data)
                data_text,key = received_tuple
                # data_text.decode('utf-8')


                print('received {!r}'.format(data))
                if data :
                    data = Cezar(data_text,key)
                    print ('sending data back to client')
                    data = data.encode('utf-8')

                    connection.sendall(data)
                else:
                    print ('not data, closing connection')
                    break
            except:EOFError

    finally:
        connection.close()