from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import Group



class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Note(models.Model):

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Category')
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True, validators=[MaxValueValidator(timezone.now)])
    reminder = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='reminder',validators=[MinValueValidator(timezone.now)])
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True,verbose_name='user')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title


