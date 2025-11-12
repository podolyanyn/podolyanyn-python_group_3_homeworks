from django.test import TestCase

# Create your tests here.
from django.contrib.gis.db.backends.spatialite import client
from django.core.exceptions import ValidationError
from django.template.defaultfilters import title
from django.test import TestCase
from .views import note_update
from django.urls import reverse

# Create your tests here.
import datetime

from django.utils import timezone

from .models import Note
from .models import Category
from django.core.validators import MinValueValidator

class NoteModelTests(TestCase):
    def test_reminder(self):
        time = timezone.now() - datetime.timedelta(days=30)
        category = Category.objects.create(category_name='Test')
        with self.assertRaises(ValidationError):
            test_note = Note(title='aaaaaa',category=category,published_date =timezone.now(),reminder=time)
            test_note.full_clean()



    def test_published_data(self):
        time = timezone.now()+ datetime.timedelta(days=30)
        time2 = timezone.now()
        category = Category.objects.create(category_name='Test')
        with self.assertRaises(ValidationError):
            test_note2 = Note(title='aaaaaa',category=category,published_date=time,reminder=time2)
            test_note2.full_clean()
"""З початку в моделях можна було створювати reminder на минулу дату і published_date на майбутню .
 Щоб виконати завдання з тестів ввів  у модель валідатори максимального і мінімального значення"""


class NoteCreateTests(TestCase):
    # def setUp(self):
    #     self.test_note=Note.objects.create(pk = 1,title = 'Тест нотатка інтеграційна',
    #     category = Category.objects.create(category_name='Test'),
    #     text = 'dsdfsfsfsfsfsf',
    #     published_date =timezone.now,
    #     reminder = timezone.now()+ datetime.timedelta(days=30))
    #
    #     self.update_url = reverse('update', args=[self.test_note.pk])



    def test_update(self):
        self.test_note = Note.objects.create(pk=1, title='Тест нотатка інтеграційна',
                                             category=Category.objects.create(category_name='Test'),
                                             text='dsdfsfsfsfsfsf',
                                             published_date=timezone.now,
                                             reminder=timezone.now() + datetime.timedelta(days=30))

        self.update_url = reverse('update', args=[self.test_note.pk])

        category_new = self.test_note.category
        title_new = 'integration note'
        # start_test = reverse('update', args=[self.test_note.pk])
        new_data = {'title':title_new,'category': str(category_new.id),'text':'hhhhh','published_date':timezone.now(),'reminder':timezone.now()}
        response = self.client.post(self.update_url, data=new_data)
        # self.test_note.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        # self.test_note.refresh_from_db()

        self.assertEqual(self.test_note.title, 'integration note')
        self.assertEqual(self.test_note.category, category_new)
        self.assertEqual(self.test_note.text, 'hhhhh')