from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cat_title = models.CharField(max_length=200)

    def __str__(self):
        return self.cat_title

class Note(models.Model):
    note_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=200)
    note_text = models.TextField()
    note_reminder = models.DateTimeField("date reminder")
    note_created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.note_title

