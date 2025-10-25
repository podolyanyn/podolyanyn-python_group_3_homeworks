from django.contrib import admin

# Register your models here.
# myapp/admin.py (колишній polls/admin.py)

from django.contrib import admin
from .models import Note
from .models import Category# Імпортуємо нову модель

# Реєструємо Note, щоб вона з'явилася в адмін-панелі
admin.site.register(Note)
admin.site.register(Category)
