

from django.db import models
from django.utils import timezone



class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Note(models.Model):

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Category')
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField(default=timezone.now,null=True,blank=True,verbose_name='reminder')

    def __str__(self):
        return self.title
