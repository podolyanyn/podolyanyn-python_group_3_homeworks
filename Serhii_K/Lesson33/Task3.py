# Task 3:
# The Weather app
# Напишіть консольний додаток, який отримує на вхід назву міста і повертає поточну погоду у вибраному вами форматі.
# Для поточного завдання ви можете вибрати будь-який метеорологічний API або веб-сайт,
# або скористатися openweathermap.org

import sys
import requests
import json
from datetime import datetime


def citys_weather(city):
    """Функція, що приймає назву міста українською мовою, і повертає погоду на поточну годину"""

    # Координати українськіх міст (обмежений список для прикладу)
    coorinates = {
    "Київ":[50.27,30.31],
    "Львів":[49.50, 24.00],
    "Харків":[50.00, 36.14],
    "Одеса":[46.29, 30.45],
    "Полтава":[49.58872406025148, 34.543482828407505],
    "Дніпро":[48.29, 35.05]
    }

    # Складаємо та відправляємо http запит, використовуючи координати заданого міста:
    if city in coorinates:
        latitude, longitude = coorinates[city]

        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,wind_speed_10m,precipitation,rain&timezone=auto&forecast_days=7'
        response = requests.get(url)

    # Якщо запит був невдалий, друкуємо повідомлення:
    if response.status_code != 200:
        result1 = "Не вдалось отримати прогноз погоди"
    # Якщо запит був вдалим, то обробляємо отримані дані:
    else:
        json_response = response.json()

        # Збереження даних до файлу 'Weather.json' - для прикладу (це не входить в умови задачі)
        with open('Weather.json', 'w', encoding='utf-8') as file:
            json.dump(json_response, file, ensure_ascii=False, indent=4)

        # З результату запиту вилучаємо списки дат/часу, значення температури, вітру, дощу, опадів:
        hourly_time = json_response["hourly"]['time']                       # Формат часу "%Y-%m-%dT%H:%M"
        hourly_temperature_2m = json_response["hourly"]['temperature_2m']   # Температура
        hourly_wind_speed_10m = json_response["hourly"]['wind_speed_10m']   # Вітер
        hourly_rain = json_response["hourly"]['rain']                       # Дощ
        hourly_precipitation = json_response["hourly"]['precipitation']     # Опади

        # Поточна дата та час
        now = datetime.now()

        # Форматуємо в формат часу "%Y-%m-%dT%H:%M (ChatGPT)
        #    %Y - рік з 4 цифр, %m - місяць, %d - день, T - літера T,
        #    %H - година (24-годинний формат), %M - хвилина
        now_string = now.strftime('%Y-%m-%dT%H:00')

        # Шукаємо потрібну дату і час в списку hourly_time і відповідні їм дані про температуту, вітер, опади:
        result = f"{city}: \n"
        if now_string in hourly_time:
            index = hourly_time.index(now_string)
            result += f"Температура {hourly_temperature_2m[index]} °C\n"
            result += f"Вітер {hourly_wind_speed_10m[index]} км/г\n"
            # Дощ, опади
            # (Спрощено - є опади чи ні. Можливо за кількістю міліметрів опадів можливо можна робити висновки про силу дощу...)
            if hourly_rain[index] == 0:
                result += f"Без опадів\n"
            else:
                result += f"Опади {hourly_rain[index]} мм\n"

    # Друк прогнозу погоди:
    print(result)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        city_name = sys.argv[1]
    else:
        city_name = "Київ"

    citys_weather(city_name)