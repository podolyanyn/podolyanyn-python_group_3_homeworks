from django.test import TestCase, Client
from django.urls import reverse
from .models import Note, Category

# Create your tests here.

class TestNote(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Test Category")
        self.client = Client()

    def test_create_note(self):
        url = reverse('create_note')
        data = {
            'title': 'Test Title',
            'text': 'Test Text',
            'reminder': '',
            'category': str(self.category.id),
        }
        response = self.client.post(url, data)


        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)
        new_note = Note.objects.first()
        self.assertEqual(new_note.title, 'Test Title')
        self.assertEqual(new_note.category, self.category)

    def test_update_note(self):
        note = Note.objects.create(title='Old Title', text='Old Text', category=self.category)
        url = reverse('note_update', args=[note.pk])
        data = {
            'title': 'New Title',
            'text': 'New Text',
            'reminder': '',
            'category': str(self.category.id),
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        note.refresh_from_db()
        self.assertEqual(note.title, 'New Title')
        self.assertEqual(note.text, 'New Text')