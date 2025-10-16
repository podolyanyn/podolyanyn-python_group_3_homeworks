from django.shortcuts import render

# Create your views here.

class Notes:
    def __init__(self, title, text, reminder, category):
        self.title = title
        self.text = text
        self.reminder = reminder
        self.category = category

notes_list = [
              Notes('notes 1', 'text notes 1', 'reminder notes 1', 'category 1'),
              Notes('notes 2', 'text notes 2', 'reminder notes 2', 'category 2'),
              Notes('notes 3', 'text notes 3', 'reminder notes 3', 'category 3')
              ]



def index(request):
    return render(request, 'notes_app/index.html', {'notes_list': notes_list})