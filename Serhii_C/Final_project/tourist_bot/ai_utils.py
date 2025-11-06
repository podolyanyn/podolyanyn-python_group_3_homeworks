import requests
import json
import time
import asyncio
from asgiref.sync import sync_to_async
# import google.generativeai as genai

API_KEY = "AIzaSyAbkDiOPIMGPJmqEOgYZ4Y1g3YYRSRloSw"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent"
async def call_gemini_api(prompt: str):
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {'Content-Type': 'application/json'}
    try:
        response = await sync_to_async(requests.post, thread_sensitive=False)(
            f"{API_URL}?key={API_KEY}",
            headers=headers,
            data=json.dumps(payload),timeout=30)
        if response.status_code == 200:
            data = response.json()
            text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text',"Не вдалося отримати відповідь від AI.")
            return text
        else:
            print(f"Помилка API ")
            return f"Вибачте, сталася помилка сервера ({response.status_code}) при спілкуванні з AI."

    except requests.exceptions.RequestException as e:
        print(f"Помилка мережі/запиту: {e}")
        return "Вибачте, сталася помилка мережі. Будь ласка, перевірте з'єднання."
