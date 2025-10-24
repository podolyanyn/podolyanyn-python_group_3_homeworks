

from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.ForeignKey(Category, on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField(default=timezone.now,null=True,blank=True,verbose_name='reminder')

    def __str__(self):
        return self.title.title
