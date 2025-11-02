from django.shortcuts import render
from .models import Note

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes_app/index.html', {'notes': notes})