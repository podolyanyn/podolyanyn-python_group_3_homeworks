# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Note


def index(request):
    notes_list = Note.objects.all().order_by('-note_updated_at')
    return render(request, 'notes/index.html', {'notes_list': notes_list})

def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/note_detail.html', {'note': note})