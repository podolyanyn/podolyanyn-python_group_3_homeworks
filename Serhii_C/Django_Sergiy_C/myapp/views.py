from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NoteForm
from .models import Note
from .models import Category
from .forms import CategoryForm

def note_list(request):
    notes = Note.objects.all().order_by('published_date')
    search_query = request.GET.get('q')
    if search_query:
        notes_found = Note.objects.filter(title__iexact=search_query)
        if notes_found.exists() and notes_found.count() == 1:
            note = notes_found.first()
            return redirect('detail', pk=note.pk)
        else:
            context = {'note': notes}
            return render(request, 'myapp/note/note_list.html', context)
        # return redirect('list', q=search_query)


    selected_category_pk = request.GET.get('category')
    print(f"Отриманий ID категорії: {selected_category_pk}")
    if selected_category_pk:
        notes = notes.filter(category__pk=selected_category_pk)
        print(f"Виконуємо фільтрацію: {notes.query}")
    categories = Category.objects.all()

    context = {
        'notes': notes,
        'categories': categories,
        'selected_category': selected_category_pk,
    }

    return render(request, 'myapp/note/note_list.html', context)

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {'note': note}
    return render(request, 'myapp/note/note_detail.html', context)




def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)

            if request.user.is_authenticated:
                note.user = request.user
            else:
                pass
            note.save()
            return redirect('list')

    elif request.method == 'GET':
        form = NoteForm()
        return render(request, 'myapp/note/note_form.html', {'form': form})

def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('detail',pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'myapp/note/note_form.html', {'form': form, 'note': note})
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('list')
    elif request.method == 'GET':
        return render(request, 'myapp/note/note_delete.html', {'note': note})

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = CategoryForm()
    return render(request, 'myapp/note/category_form.html', {'form': form})

def search(request):
    for notes in Note.objects.all():
        if notes.title==request.GET.get('title'):
            note_detail(request,notes.pk)
            return render(request, 'myapp/note/note_detail.html', {'note': notes})