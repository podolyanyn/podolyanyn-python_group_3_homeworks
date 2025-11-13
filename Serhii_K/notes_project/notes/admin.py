from django.contrib import admin

from .models import Category, Note

class NoteInline(admin.TabularInline):
    model = Note
    fields = ["note_title"]
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Категорія", {"fields": ["cat_title"]}),
    ]
    inlines = [NoteInline]


class NoteAdmin(admin.ModelAdmin):
    fields = ["note_title", "note_category", "note_text", "note_reminder", "author"]
    list_display = ["note_title", "note_category", "note_created_at", "note_reminder", "author"]
    list_filter = ["note_category", "note_reminder", "author"]
    search_fields = ["note_title", "note_text", "author"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)