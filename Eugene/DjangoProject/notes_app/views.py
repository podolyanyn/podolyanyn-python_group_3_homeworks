from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Note
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes_app/index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Note.objects.all()
        return Note.objects.filter(user=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/create_note.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes_app/detail.html'
    context_object_name = 'note'

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser:
            return obj
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes_app/update.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Note.objects.all()
        return Note.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser:
            return obj
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes_app/delete.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Note.objects.all()
        return Note.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_superuser:
            return obj
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class UserLoginView(LoginView):
    template_name = 'notes_app/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('index')
