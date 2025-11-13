import requests

url_1 = 'https://uk.wikipedia.org/robots.txt'
url_2 = 'https://twitter.com/robots.txt'

headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

result_1 = requests.get(url_1, headers=headers)
result_2 = requests.get(url_2, headers=headers)

if result_1.ok:
    with open("robots_wiki.txt", "wb") as file_1:
        file_1.write(result_1.content)
else:
    print(f'Error: {result_1.status_code}')

if result_2.ok:
    with open("robots_twit.txt", "wb") as file_2:
        file_2.write(result_2.content)
else:
    print(f'Error: {result_2.status_code}')