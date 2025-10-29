from django import forms
from .models import Category


class Add_note_form(forms.Form):
    note_title = forms.CharField(label="Назва нотатки", max_length=100)
    note_text = forms.CharField(label="Текст нотатки", widget=forms.Textarea)
    note_category = forms.CharField(label="Категорія нотатки", max_length=100)
    note_reminder = forms.DateTimeField(label="Дата нагадування", input_formats=["%Y-%m-%d %H:%M"], widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))

class Edit_note_form(forms.Form):
    note_title = forms.CharField(label="Назва нотатки", max_length=200)
    note_text = forms.CharField(label="Текст нотатки", widget=forms.Textarea)
    note_category = forms.CharField(label="Категорія нотатки", max_length=200)
    note_reminder = forms.DateTimeField(
        label="Дата нагадування",
        input_formats=["%Y-%m-%d %H:%M"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )