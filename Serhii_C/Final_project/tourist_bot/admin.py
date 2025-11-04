

# Register your models here.
# admin.site.register(Excursion)

from django.contrib import admin
from .models import Excursion  # Імпортуємо вашу модель


# Створюємо клас, щоб налаштувати вигляд адмінки
# Це наш "командний центр" для моделі Excursion в адмін-панелі
@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    # 1. Що відображати у списку (колонки)
    list_display = ('title', 'type', 'is_lunch_included', 'price', 'keyword')

    # 2. Фільтри (бічні панелі для швидкого пошуку)
    list_filter = ('type', 'is_lunch_included')

    # 3. Поля для пошуку (пошуковий рядок у верхній частині)
    # Включаємо всі великі текстові поля, щоб AI міг знайти все.
    search_fields = ('title', 'description', 'keyword', 'conditions', 'vidguki')

    # 4. Групування полів у формі редагування (для зручності)
    fieldsets = (
        # Блок 1: Загальна інформація
        ('Основні дані', {
            'fields': ('title', 'type', 'price')
        }),
        # Блок 2: Опис та AI-ключові слова
        ('Детальний опис та Ключові слова для AI', {
            'fields': ('description', 'keyword')
        }),
        # Блок 3: Умови, оплата та відгуки
        ('Умови та Додаткова інформація', {
            'fields': ('is_lunch_included', 'conditions', 'vidguki')
        }),
    )

    # Додамо функцію для відображення назви об'єкта
    def get_object_display(self, obj):
        return str(obj)

    get_object_display.short_description = 'Назва'
