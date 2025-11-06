# from django.test import TestCase
# from tourist_bot.models import Excursion
# from tourist_bot.views import excursions_list
# import asyncio
# from asgiref.sync import sync_to_async
#
#
# # !!! ВАЖЛИВО !!!
# # Якщо ви використовуєте Django < 3.1, цей тест може не працювати, оскільки Django
# # почав підтримувати async def тести лише з версії 3.1.
# # На Python 3.13, який видно у ваших трасуваннях, має бути підключена сучасна версія Django.
#
# class ExcursionListTest(TestCase):
#     """
#     Тести для перевірки асинхронної функції excursions_list у views.py.
#     """
#
#     @classmethod
#     def setUpTestData(cls):
#         # Створюємо тестовий об'єкт екскурсії, який буде збережений у тестовій БД.
#         # Це синхронна операція, яка виконується один раз для всього класу тестів.
#         cls.excursion = Excursion.objects.create(
#             title="Тестова Екскурсія Центром",
#             type=1,  # Припускаємо, що 1 відповідає певному типу (наприклад, 'Пішохідна'),
#             price=850.50,
#             is_lunch_included=True,
#             keyword="центр, історія, архітектура",
#             description="Тестовий опис для перевірки промпту.",
#             conditions="Необхідна попередня оплата на сайті.",
#             vidguki="4.9/5 зірок. Клієнти задоволені."
#         )
#
#     async def test_01_excursions_list_returns_correct_prompt(self):
#         """
#         Перевіряє, чи функція excursions_list успішно отримує дані з БД (асинхронно)
#         і формує фінальний промпт, що містить системні інструкції, дані та запит.
#         """
#
#         test_query = "Чи є обід включеним і яка ціна?"
#
#         # Викликаємо асинхронну функцію як await
#         final_prompt = await excursions_list(test_query)
#
#         # 1. Перевірка наявності ключових елементів промпту
#         self.assertIn("ТИ AI-АСИСТЕНТ ТУРИСТИЧНОГО БОТА.", final_prompt)
#         self.assertIn("--- КОНТЕКСТ З БАЗИ ДАНИХ ---", final_prompt)
#         self.assertIn("--- ЗАПИТ КОРИСТУВАЧА ---\nЧи є обід включеним і яка ціна?", final_prompt)
#         self.assertTrue(final_prompt.endswith("\n--- ВІДПОВІДЬ:"))
#
#         # 2. Перевірка наявності даних екскурсії
#         self.assertIn("НАЗВА: Тестова Екскурсія Центром", final_prompt)
#         self.assertIn("ЦІНА: 850.5", final_prompt)
#         self.assertIn("ОБІД включено: Так", final_prompt)
#         self.assertIn("Ключові слова (для пошуку): центр, історія, архітектура", final_prompt)
#
#     async def test_02_empty_excursion_data_handling(self):
#         """
#         Тестує, як функція обробляє відсутність даних (хоча QuerySet.all() завжди
#         поверне QuerySet, це перевіряє поведінку, якщо б ми могли очистити БД).
#         Тут ми просто перевіряємо, що функція повертає рядок.
#         """
#
#         # Очищаємо тестову БД для цього конкретного тесту
#         await sync_to_async(Excursion.objects.all().delete)()
#
#         test_query = "Покажи всі екскурсії"
#         final_prompt = await excursions_list(test_query)
#
#         # Перевіряємо, що промпт все одно містить інструкції та запит
#         self.assertIn("ТИ AI-АСИСТЕНТ ТУРИСТИЧНОГО БОТА.", final_prompt)
#         self.assertIn(test_query, final_prompt)
#         self.assertTrue(final_prompt.endswith("\n--- ВІДПОВІДЬ:"))
#
#         # Повертаємо дані для інших тестів
#         await sync_to_async(self.setUpTestData)()
#
#
# from django.test import TestCase
#
# # Create your tests here.

from django.test import TestCase
from tourist_bot.models import Excursion
from tourist_bot.views import excursions_list
import asyncio
from asgiref.sync import sync_to_async


class ExcursionListTest(TestCase):
    """
    Тести для перевірки асинхронної функції excursions_list у views.py.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Створюємо тестовий запис екскурсії у базі.
        """
        cls.excursion = Excursion.objects.create(
            title="Тестова Екскурсія Центром",
            type=1,  # Припускаємо, що 1 — це якийсь тип (наприклад, "Пішохідна")
            price=850.50,
            is_lunch_included=True,
            keyword="центр, історія, архітектура",
            description="Тестовий опис для перевірки промпту.",
            conditions="Необхідна попередня оплата на сайті.",
            vidguki="4.9/5 зірок. Клієнти задоволені."
        )

    async def test_01_excursions_list_returns_correct_prompt(self):
        """
        Перевіряє, чи функція excursions_list формує правильний промпт
        з урахуванням даних з бази та тексту системної інструкції.
        """
        test_query = "Чи є обід включеним і яка ціна?"
        final_prompt = await excursions_list(test_query)

        # 1️⃣ Перевіряємо, що у промпті є системна інструкція
        self.assertIn("Ти є AI-асистент туристичної компанії", final_prompt)

        # 2️⃣ Перевіряємо, що є основні частини структури
        self.assertIn("--- КОНТЕКСТ З БАЗИ ДАНИХ ---", final_prompt)
        self.assertIn("--- ЗАПИТ КОРИСТУВАЧА ---", final_prompt)
        self.assertIn(test_query, final_prompt)

        # 3️⃣ Перевіряємо, що дані екскурсії дійсно потрапили у текст
        self.assertIn("Заголовок: Тестова Екскурсія Центром", final_prompt)
        self.assertIn("Ціна: 850.5", final_prompt)
        self.assertIn("Обід включено: Так", final_prompt)
        self.assertIn("Ключові слова (для пошуку): центр, історія, архітектура", final_prompt)

        # 4️⃣ Перевірка кінцевого формату — промпт має бути рядком
        self.assertIsInstance(final_prompt, str)
        self.assertGreater(len(final_prompt), 100)

    async def test_02_empty_excursion_data_handling(self):
        """
        Перевіряє, що функція коректно працює навіть якщо у базі немає екскурсій.
        """
        # Очищаємо тестову таблицю
        await sync_to_async(Excursion.objects.all().delete)()

        test_query = "Покажи всі екскурсії"
        final_prompt = await excursions_list(test_query)

        # Перевірка, що основна структура все одно зберігається
        self.assertIn("Ти є AI-асистент туристичної компанії", final_prompt)
        self.assertIn("--- КОНТЕКСТ З БАЗИ ДАНИХ ---", final_prompt)
        self.assertIn("--- ЗАПИТ КОРИСТУВАЧА ---", final_prompt)
        self.assertIn(test_query, final_prompt)

        # Має бути валідний рядок (навіть якщо контекст пустий)
        self.assertIsInstance(final_prompt, str)
        self.assertGreater(len(final_prompt), 50)

        # Відновлюємо дані для можливих наступних тестів
        await sync_to_async(self.setUpTestData)()





import asyncio
from django.test import TestCase
from tourist_bot.models import Excursion
from tourist_bot.views import excursions_list
from tourist_bot.ai_utils import call_gemini_api



class GeminiIntegrationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.excursion = Excursion.objects.create(
            title="Тестова екскурсія Подолом",
            type=1,
            price=700,
            is_lunch_included=True,
            keyword="поділ, історія, старе місто",
            description="Це короткий тестовий опис для AI.",
            conditions="Оплата на місці або онлайн.",
            vidguki="5/5. Чудова екскурсія!"
        )

    def test_ai_response_generation(self):
        """Перевіряє, що Gemini API правильно обробляє prompt із БД"""
        async def run_test():
            user_query = "Яку екскурсію порадите для любителів архітектури?"
            prompt = await excursions_list(user_query)
            response = await call_gemini_api(prompt)

            self.assertIsInstance(response, str)
            self.assertTrue(len(response) > 10, "AI повернув занадто коротку відповідь")

        asyncio.run(run_test())

