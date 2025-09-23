import requests
import threading


#-------------------------------------------------------- 1 ------------------------------------------------------------
"""Task 1

Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc. """
URLS_DICT = {
    'wikipedia': "https://en.wikipedia.org/robots.txt",
    'x_com':"https://x.com/robots.txt",
    'beetroot':"https://beetroot.academy/robots.txt",
    'dou': "https://dou.ua/robots.txt"
}

HEADERS = {
    "User-Agent": "MyBot/1.0 (+https://example.com/bot-info)"  # свій ідентифікатор
}

def get_robots(url_key, url_addr):
    response = requests.get(url_addr, headers=HEADERS)
    with open(f'{url_key}.txt', 'w', encoding='utf-8') as fo:
        fo.write(response.text)

threads_list = []
for url_key, url_addr in URLS_DICT.items():
    t = threading.Thread(target=get_robots, args=(url_key, url_addr,))
    threads_list.append(t)
    t.start()


for t in threads_list:
    t.join()

print("------>All files were downloaded")

