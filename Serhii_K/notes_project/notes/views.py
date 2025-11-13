from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Note, Category
from .forms import Add_note_form, Edit_note_form

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required

class IndexView(generic.ListView):
    template_name = "notes/index.html"
    context_object_name = "notes_list"

    def get_queryset(self):
        return Note.objects.all().order_by('-note_created_at')


# Дозвіл на перегляд нотатки тільки автору після входу. UserPassesTestMixin дозволяє робити перевірку (ChatGPT)
class DetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    # Функція перевіряє що користувач є автором нотатки
    def test_func(self):
        note = self.get_object()
        return note.author == self.request.user


@login_required
@permission_required("notes.add_note")
def add_note(request):
    if request.method == "POST":
        form = Add_note_form(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data["note_category"]
            note_title = form.cleaned_data["note_title"]
            note_text = form.cleaned_data["note_text"]
            note_reminder = form.cleaned_data["note_reminder"]
            author=request.user     # додаємо поле author - це поточний користувач
            category, created = Category.objects.get_or_create(cat_title=category_name)
            new_note = Note(
                note_category=category,
                note_title=note_title,
                note_text=note_text,
                note_reminder=note_reminder,
                author=author,
            )
            new_note.save()
            return redirect("notes:index")
    else:
        form = Add_note_form()

    return render(request, "notes/add_note.html", {"form": form})

@login_required
@permission_required("notes.change_note")
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    # Якщо користувач не є автором нотатки - відправляємо його на сторінку Помилка 403 (ChatGPT)
    if note.author != request.user:
        return render(request, "notes/forbidden.html", status=403)

    if request.method == "POST":
        form = Edit_note_form(request.POST)
        if form.is_valid():
            # note.save(commit=False)   #Чередніченко
            note.note_title = form.cleaned_data["note_title"]
            note.note_text = form.cleaned_data["note_text"]
            note.note_reminder = form.cleaned_data["note_reminder"]
            category_name = form.cleaned_data["note_category"]
            category, created = Category.objects.get_or_create(cat_title=category_name)
            note.note_category = category

            note.save()
            return redirect("notes:note_detail", pk=note.id)
    else:
        # Початкові дані для форми
        form = Edit_note_form(initial={
            "note_title": note.note_title,
            "note_text": note.note_text,
            "note_category": note.note_category,
            "note_reminder": note.note_reminder.strftime("%Y-%m-%d %H:%M"),
        })

    return render(request, "notes/edit_note.html", {"form": form, "note": note})

@login_required
@permission_required("notes.delete_note")
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    # Якщо користувач не є автором нотатки - відправляємо його на сторінку Помилка 403 (ChatGPT)
    if note.author != request.user:
        return render(request, "notes/forbidden.html", status=403)

    if request.method == "POST":
        note.delete()
        return redirect("notes:index")

    return redirect("notes:index")
