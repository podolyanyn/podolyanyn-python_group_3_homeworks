from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    text = models.TextField(verbose_name="Note text")
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Reminder")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"