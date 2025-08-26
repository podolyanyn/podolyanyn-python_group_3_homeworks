import requests
response = requests.get("http://pravda.com.ua")
print(response.status_code)
print(response.text)