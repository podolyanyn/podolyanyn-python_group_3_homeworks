from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime
from .models import Note, Category


# Тести функції add_note:
class Test_add_notes(TestCase):
    def test_add_notes(self):
        """Тест для перевірки функції створення нової нотатки - add_note (views.py)"""

        # Дані, які потрібні передати в форми під час створення нової нотатки:
        new_note_data = {
            "note_category":"new_category",
            "note_title":"тестова нотатка",
            "note_text":"тестова нотатка для перевірки",
            "note_reminder":"2026-11-30 10:00",
            }

        # Отримуємо url до сторінки add_note:
        my_url = reverse('notes:add_note')

        # Надсилаємо дані new_note_data до view add_note через POST-запит:
        response = self.client.post(my_url, data=new_note_data)

        # Після створення нотатки має відкритись сторінка index
        self.assertRedirects(response, reverse("notes:index"))

        # Перевірка створенної категорії:
        self.assertEqual(Category.objects.first().cat_title, "new_category")

        # Перевірка створенної нотатки:
        note = Note.objects.first()
        self.assertEqual(note.note_category.cat_title, "new_category")
        self.assertEqual(note.note_title, "тестова нотатка")
        self.assertEqual(note.note_text, "тестова нотатка для перевірки")

        # Перевірка виду: self.assertEqual(str(note.note_reminder), "2026-11-30 10:00") - не працює,
        # бо в налаштуванні settings.py TIME_ZONE = 'Europe/Kyiv',
        # і київський час відрізняється на 2 години від UTC,
        # тому перевіряємо лише рік, місяць, дату:
        self.assertEqual(note.note_reminder.year, 2026)
        self.assertEqual(note.note_reminder.month, 11)
        self.assertEqual(note.note_reminder.day, 30)


# Тести функції edit_note:
class Test_note_edit(TestCase):
    def test_edit_note(self):
        """Тест для перевірки функції редагування нотатки - edit_note (views.py)"""

        # Спочатку створюємо категорію, до якої прив'яжемо перший варіант нотатки:
        old_category = Category.objects.create(cat_title="Існуюча категорія")
        old_category.save()

        # Створення нотатки, яку потім будемо змінювати:
        old_note = Note.objects.create(
            note_category=old_category,
            note_title="Існуюча нотатка",
            note_text="Існуючий текст нотатки",
            note_reminder="2026-11-30 10:00"
        )
        old_note.save()

        # Дані, які потрібні передати в форми під час створення нової нотатки:
        new_note_data = {
            "note_category":"змінена категорія",
            "note_title":"змінена нотатка",
            "note_text":"змінений текст нотатки",
            "note_reminder":"2026-12-30 10:00",     # Змінюємо тільки місяць дати нагадування
            }

        # Отримуємо url до сторінки add_note:
        my_url = reverse('notes:edit_note', args=[old_note.id])

        # Надсилаємо дані new_note_data до view add_note через POST-запит:
        response = self.client.post(my_url, data=new_note_data)

        # Перевірка створенної нотатки:
        note = Note.objects.first()
        # Після створення нотатки має відкритись сторінка note_detail
        self.assertRedirects(response, reverse("notes:note_detail", args=[note.id]))

        # Перевірка створенної нотатки:
        note = Note.objects.first()
        self.assertEqual(note.note_category.cat_title, "змінена категорія")
        self.assertEqual(note.note_title, "змінена нотатка")
        self.assertEqual(note.note_text, "змінений текст нотатки")
        self.assertEqual(note.note_reminder.month, 12)  # Перевіряємо місяць дати нагадування


# Тести відображення index:
class Note_Index_View_Tests(TestCase):
    def test_no_notes(self):
        """Тест перевіряє чи відображається на сторінці index повідомлення:
        'No notes are available.', якщо жодна нотатка не створена"""

        response = self.client.get(reverse("notes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No notes are available.")
        self.assertQuerySetEqual(response.context["notes_list"], [])

    def test_created_notes(self):
        """Тест перевіряє чи зберігаються нові нотатки в базі даних"""

        # Створення нової категорії
        new_category = Category.objects.create(cat_title="Тестова категорія")

        # Створення нової нотатки, пов'язаної з тестовою категорією, і з часом нагадування через 1 день в майбутньому
        time = timezone.now() + datetime.timedelta(days=1)
        new_note = Note.objects.create(note_text="Тестова нотатка для перевірки чи зберігаются нотатки в базі даних", note_category=new_category, note_reminder=time)

        # Перевірка чи відображається нова нотатка на сторінці index:
        response = self.client.get(reverse("notes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["notes_list"], [new_note])