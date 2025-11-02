from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm

class NoteListView(ListView):
    model = Note
    template_name = 'notes_app/index.html'
    context_object_name = 'notes'

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/create_note.html'
    success_url = reverse_lazy('index')

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes_app/detail.html'
    context_object_name = 'note'


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/update.html'

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes_app/delete.html'
    context_object_name = 'note'
    success_url = reverse_lazy('index')