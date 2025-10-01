# Завдання 1
#
# Спільний лічильник
#
# Створіть клас під назвою Counter та зробіть його підкласом класу Thread у модулі Threading.
# Зробіть клас з двома глобальними змінними: однією під назвою counter, встановленою на 0, та іншою під назвою rounds,
# встановленою на 100.000. Тепер реалізуйте метод run(), нехай він включає простий цикл for, який перебирає раунди
# (наприклад, 100.000 разів) і для кожного разу збільшує значення лічильника на 1.
# Створіть 2 екземпляри потоку та запустіть їх, потім об('єднайте їх та перевірте результат лічильника,'
#  він має бути 200.000, чи не так? Запустіть його кілька разів та розгляньте різні причини, чому ви отримуєте таку відповідь.)
# import threading
# counter =0
# rounds = 100000
#
# class My_potoks(threading.Thread):
#     def __init__(self, counter, rounds):
#
#         super().__init__()
#
#         self.counter = counter
#         self.rounds = rounds
#
#
#     def run(self):
#         global counter
#         for i in range(rounds):
#             counter=counter+1
#         return counter
# first_potok = My_potoks(counter,rounds)
# second_potok = My_potoks(counter,rounds)
# first_potok.start()
# second_potok.start()
# first_potok.join()
# second_potok.join()
# print(first_potok)
# print(second_potok)
# print(counter)#  так counter досяг 200000 у 3х з 3 спробах.

# # Завдання 2
# #
# # Echo-сервер з потоками
# #
# # Створіть socket echo-сервер, який обробляє кожне з'єднання в окремому потоці
import requests
import threading
import pickle

def get_currency_info(start_date, end_date, currency,connection):


    response = requests.get(f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={currency}&sort=exchangedate&order=desc&json')
    if response.status_code == 200:
        print(f'Дані по {currency} отримано')
        # print(response.json())
    for_sending = []
    for element in response.json():
        currency_name = element['enname']
        day = element['exchangedate']
        rate = element['rate']
        for_sending.append((currency_name,day, rate))
    # print(for_sending)
    data_for_sending = pickle.dumps(for_sending)
    connection.sendall(data_for_sending)
    print(f'Данні по {currency} відправлені')
    connection.close()





import pickle
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8082)
print ('start with {} port{}'.format(*server_address))
sock.bind(server_address)
sock.listen(5)
while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)
    data = connection.recv(1024)
    received_tuple = pickle.loads(data)
    start_date, end_date, currency = received_tuple
    t = threading.Thread(target=get_currency_info, args=(start_date, end_date, currency,connection))
    t.start()
    print (f'Потік для {currency} почався')


# # Завдання 3
# # Запити з використанням багатопоточності
# # Завантажте всі коментарі з вибраного вами subreddit за допомогою URL-адреси: https://api.pushshift.io/reddit/comment/search/ .
# # В результаті збережіть усі коментарі в хронологічному порядку у форматі JSON та виведіть їх у файл.
# # Для цього завдання використовуйте Threads для здійснення запитів до API reddit.
#
# import requests
# import json
# import threading
#
# def fetch_nbu_data(start,end):
#     """Отримання даних з API НБУ"""
#     base_url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/grossextdebt?{start}=20160301&{end}=20170601&json"
#
#     response = requests.get(base_url)
#     print(response.json())
#
#
#
#     with open("data_for.json", "w", encoding="utf-8") as f:
#         json.dump(response.json(), f, ensure_ascii=False, indent=4)
# t = threading.Thread(target=fetch_nbu_data, args=(20160301,20170601))
# t.start()