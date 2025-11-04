from asgiref.sync import sync_to_async
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import Note, Category
from .forms import Add_note_form, Edit_note_form

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required


import time
# Декоратор для вимірювання часу виконання
def my_decorator_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Time ({func.__name__}): {time.time()-start_time}")
        return result
    return wrapper

# Асинхронний варіант декоратора
def my_async_decorator_time(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Time ({func.__name__}): {time.time()-start_time}")
        return result
    return wrapper


# class IndexView(generic.ListView):
#     template_name = "notes/index.html"
#     context_object_name = "notes_list"
#
#     def get_queryset(self):
#         return Note.objects.all().order_by('-note_created_at')

# Замість IndexView.as_view(pk) зроблено функцію detail_note(request, pk),
# яка дозволяє перевірити час виконання за допомогою декоратора @my_decorator_time
@my_decorator_time
def index(request):
    notes_list = Note.objects.all().order_by('-note_created_at')
    context_object_name = {"notes_list": notes_list}
    return render(request, "notes/index.html", context_object_name)

@my_async_decorator_time
async def index(request):
    # Oбгортаємо в sync_to_async
    notes_list = await sync_to_async(Note.objects.all().order_by)('-note_created_at')
    context_object_name = {"notes_list": notes_list}
    return await sync_to_async(render)(request, "notes/index.html", context_object_name)



# Дозвіл на перегляд нотатки тільки автору після входу. UserPassesTestMixin дозволяє робити перевірку (ChatGPT)
# class DetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
#     model = Note
#     template_name = "notes/detail_note.html"
#
#     # Функція перевіряє що користувач є автором нотатки
#     def test_func(self):
#         note = self.get_object()
#         return note.author == self.request.user



# Замість DetailView.as_view(pk) зроблено функцію detail_note(request, pk),
# яка дозволяє перевірити час виконання за допомогою декоратора @my_decorator_time
@my_decorator_time
# @login_required
# @permission_required("notes.detail_note")
def detail_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    # # Якщо користувач не є автором нотатки - відправляємо його на сторінку Помилка 403
    # if note.author != request.user:
    #     context_403 = {"message": f"Ви не є автором нотатки '{note.note_title}'."}
    #     return render(request, "notes/forbidden.html", status=403, context=context_403, )

    # Якщо користувач є автором (все ОК):
    context = {'note': note}
    return render(request, "notes/detail_note.html", context)


@my_async_decorator_time
# @login_required
async def detail_note(request, pk):
    note = await sync_to_async(get_object_or_404)(Note, pk=pk)

    # # Перевірка автора
    # if note.author != request.user:
    #     context_403 = {"message": f"Ви не є автором нотатки '{note.note_title}'."}
    #     return await sync_to_async(render)(request, "notes/forbidden.html", status=403, context=context_403)

    # Якщо користувач є автором (все ОК):
    context = {'note': note}
    return await sync_to_async(render)(request, "notes/detail_note.html", context)




@my_decorator_time
# @login_required
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


@my_async_decorator_time
# @login_required
async def add_note(request):
    if request.method == "POST":
        # 1. Ініціалізація форми та валідація
        form = await sync_to_async(Add_note_form)(request.POST)
        if await sync_to_async(form.is_valid)():
            # Отримання даних з форми
            cleaned_data = await sync_to_async(lambda: form.cleaned_data)()
            category_name = cleaned_data["note_category"]
            note_title = cleaned_data["note_title"]
            note_text = cleaned_data["note_text"]
            note_reminder = cleaned_data["note_reminder"]

            author = await sync_to_async(lambda: request.user)()

            category, created = await sync_to_async(Category.objects.get_or_create)(cat_title=category_name)

            new_note = await sync_to_async(Note)(
                note_category=category,
                note_title=note_title,
                note_text=note_text,
                note_reminder=note_reminder,
                author=author,
            )

            await sync_to_async(new_note.save)()

            return await sync_to_async(redirect)("notes:index")
    else:
        form = await sync_to_async(Add_note_form)()

    return await sync_to_async(render)(request, "notes/add_note.html", {"form": form})




@my_decorator_time
# @login_required
# @permission_required("notes.change_note")
def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    # Якщо користувач не є автором нотатки - відправляємо його на сторінку Помилка 403
    if note.author != request.user:
        context_403 = {"message": f"Ви не є автором нотатки '{note.note_title}'."}
        return render(request, "notes/forbidden.html", status=403, context=context_403, )

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
            return redirect("notes:detail_note", pk=note.id)
    else:
        # Початкові дані для форми
        form = Edit_note_form(initial={
            "note_title": note.note_title,
            "note_text": note.note_text,
            "note_category": note.note_category,
            "note_reminder": note.note_reminder.strftime("%Y-%m-%d %H:%M"),
        })

    return render(request, "notes/edit_note.html", {"form": form, "note": note})

@my_async_decorator_time
# @login_required
# @permission_required("notes.change_note")
async def edit_note(request, note_id):
    note = await sync_to_async(get_object_or_404)(Note, pk=note_id)

    # Перевірка автора
    # if note.author != request.user:
    #     context_403 = {"message": f"Ви не є автором нотатки '{note.note_title}'."}
    #     return await sync_to_async(render)(request, "notes/forbidden.html", status=403, context=context_403)

    if request.method == "POST":
        # 1. Ініціалізація форми з POST-даними
        form = await sync_to_async(Edit_note_form)(request.POST)

        if await sync_to_async(form.is_valid)():
            # 2. УСПІХ: Обробка та редирект
            note.note_title = form.cleaned_data["note_title"]
            note.note_text = form.cleaned_data["note_text"]
            note.note_reminder = form.cleaned_data["note_reminder"]

            category_name = form.cleaned_data["note_category"]
            category, created = await sync_to_async(Category.objects.get_or_create)(cat_title=category_name)
            note.note_category = category

            await sync_to_async(note.save)()
            return await sync_to_async(redirect)("notes:detail_note", pk=note.id)
    else:  # GET-запит
        # 1. Безпечна обробка reminder
        reminder_value = note.note_reminder.strftime("%Y-%m-%d %H:%M") if note.note_reminder else ""

        # 2. Безпечна обробка category
        category_obj = await sync_to_async(lambda: note.note_category)()
        category_value = category_obj.cat_title if category_obj else ""

        # 3. Ініціалізація форми з початковими даними
        form = await sync_to_async(Edit_note_form)(initial={
            "note_title": note.note_title,
            "note_text": note.note_text,
            "note_category": category_value,
            "note_reminder": reminder_value,
        })

    return await sync_to_async(render)(request, "notes/edit_note.html", {"form": form, "note": note})


@my_decorator_time
# @login_required
# @permission_required("notes.delete_note")
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    # Якщо користувач не є автором нотатки - відправляємо його на сторінку Помилка 403
    if note.author != request.user:
        context_403 = {"message": f"Ви не є автором нотатки '{note.note_title}'."}
        return render(request, "notes/forbidden.html", status=403, context=context_403, )

    if request.method == "POST":
        note.delete()
        return redirect("notes:index")

    return redirect("notes:index")


@my_async_decorator_time
# @login_required
# @permission_required("notes.delete_note")
async def delete_note(request, note_id):
    note = await sync_to_async(get_object_or_404)(Note, pk=note_id)

    # Перевірка автора
    if note.author != request.user:
        context_403 = {"message": f"Ви не є автором нотатки '{note.note_title}'."}
        return await sync_to_async(render)(request, "notes/forbidden.html", status=403, context=context_403)

    if request.method == "POST":
        await sync_to_async(note.delete)()
        return await sync_to_async(redirect)("notes:index")

    return await sync_to_async(redirect)("notes:index")