from django.shortcuts import render
from .models import Excursion
from .models import Excursion  # Імпортуємо вашу модель
from django.db.models.query import QuerySet
from typing import List, Dict, Any, Union,Iterable
# from gemini_api import generate_ai_response  # Місце для майбутнього імпорту AI
from asgiref.sync import sync_to_async
import asyncio


def prepering_data_for_ai(excursions: Iterable[Excursion]):
    context_parts = []
    for excursion in excursions:
        type_display = excursion.get_type_display()
        excursion_block = (
            f"--- ПОЧАТОК ЕКСКУРСІЇ: {excursion.title} ---\n"
            f"Заголовок: {excursion.title}\n"
            f"Тип: {type_display}\n"
            f"Ціна: {excursion.price}\n"
            f"Обід включено: {'Так' if excursion.is_lunch_included else 'Ні'}\n"
            f"Ключові слова (для пошуку): {excursion.keyword}\n"
            f"\n"
            f"Детальний опис:\n{excursion.description}\n"
            f"\n"
            f"Умови і оплата (включно з посиланнями): \n{excursion.conditions}\n"
            f"\n"
            f"Відгуки клієнтів: \n{excursion.vidguki}\n"
            f"--- КІНЕЦЬ ЕКСКУРСІЇ ---\n"
        )
        context_parts.append(excursion_block)
    return "\n\n".join(context_parts)


async def excursions_list(user_query):

    excursions_gotten_fromBD = await sync_to_async(list)(Excursion.objects.all())
    # excursions_gotten_fromBD = await sync_to_async(Excursion.objects.all)()
    # excursions_list = list(excursions_gotten_fromBD)
    # excursions_gotten_fromBD = await sync_to_async(Excursion.objects.all, thread_sensitive=False)()
    # excursions_list = await sync_to_async(list, thread_sensitive=False)(excursions_gotten_fromBD)
    excursions_context = prepering_data_for_ai(excursions_gotten_fromBD)

    system_instruction = (
        "Ти є AI-асистент туристичної компанії. Твоє завдання — аналізувати надані "
        "дані екскурсій та відповідати на запитання користувача. "
        "Відповідай дружнім, інформативним тоном і використовуй лише надану інформацію. "
        "Якщо користувач питає про ціну або посилання на оплату, обов'язково надай точну інформацію з даних."
    )

    final_prompt = (
        f"СИСТЕМНА ІНСТРУКЦІЯ: {system_instruction}\n\n"
        f"--- КОНТЕКСТ З БАЗИ ДАНИХ ---\n"
        f"{excursions_context}\n\n"
        f"--- ЗАПИТ КОРИСТУВАЧА ---\n"
        f"{user_query}"
    )
    return final_prompt
