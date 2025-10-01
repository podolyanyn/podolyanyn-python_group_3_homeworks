# Task 1:
# Robots.txt
# Завантажте та збережіть файл robots.txt з вікіпедії, твіттера тощо.


import requests

url_1 = "https://uk.wikipedia.org/robots.txt"   # вікіпедія
url_2 = "https://twitter.com/robots.txt"        # твіттер

# Додаємо заголовок User-Agent (інакше отримуємо код статуса 403 - відмова сервера) - (ChatGPT)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Отримуємо дані з вікіпедії:
response = requests.get(url_1, headers=headers)
# Зберігаємо в файл
with open('wiki_robot.txt', "wb") as file: # параметр wb - запис в бінарному режимі
    file.write(response.content)

# Отримуємо дані з твіттера:
response = requests.get(url_2, headers=headers)
# Зберігаємо в файл
with open('twitter_robot.txt', "wb") as file:
    file.write(response.content)