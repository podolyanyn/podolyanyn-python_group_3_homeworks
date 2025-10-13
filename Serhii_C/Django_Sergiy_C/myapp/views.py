# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Привіт, світ! Це мій перший Django-додаток.")
