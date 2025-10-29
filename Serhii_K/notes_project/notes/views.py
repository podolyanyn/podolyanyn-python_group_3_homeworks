# from django.http import HttpResponse
# from django.template import loader
from datetime import datetime, timedelta

from django.db.models import F
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Note, Category
from .forms import Add_note_form, Edit_note_form



class IndexView(generic.ListView):
    template_name = "notes/index.html"
    context_object_name = "notes_list"

    def get_queryset(self):
        return Note.objects.all().order_by('-note_created_at')


class DetailView(generic.DetailView):
    model = Note
    template_name = "notes/note_detail.html"


def add_note(request):
    if request.method == "POST":
        form = Add_note_form(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data["note_category"]
            note_title = form.cleaned_data["note_title"]
            note_text = form.cleaned_data["note_text"]
            note_reminder = form.cleaned_data["note_reminder"]
            category, created = Category.objects.get_or_create(cat_title=category_name)
            new_note = Note(
                note_category=category,
                note_title=note_title,
                note_text=note_text,
                note_reminder=note_reminder,
            )
            new_note.save()
            return redirect("notes:index")
    else:
        form = Add_note_form()

    return render(request, "notes/add_note.html", {"form": form})


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
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

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.method == "POST":
        note.delete()
        return redirect("notes:index")

    return redirect("notes:index")