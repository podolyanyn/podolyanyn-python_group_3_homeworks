from django import forms
from .models import Note
from .models import Category

class NoteForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder','category']

class CategoryForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = Category
        fields = ['category_name']