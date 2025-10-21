# # myapp/views.py

# from django.shortcuts import render
# from django.http import HttpResponse

# # def home_page(request):
# #     return HttpResponse("Привіт, світ! Це мій перший Django-додаток.")

# class Notes:
#     def __init__(self,page_head):
#         self.page_head = page_head

# latest_notes_list = [Notes('Note 1'), Notes('Note 2'), Notes('Note 3')]

# def index(request):
#     # latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.page_head for q in latest_notes_list])
#     return HttpResponse(output)

# def note1(request, question_id):
#     return HttpResponse("Page1 %s." % question_id)


# def note2(request, question_id):
#     response = "Page2  %s."
#     return HttpResponse(response % question_id)


# def note3(request, question_id):
#     return HttpResponse("Page3  %s." % question_id)


# myapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Note
from .models import Category

def note_list(request):
    notes = Note.objects.all().order_by('published_date')
    context = {'notes': notes}
    return render(request, 'myapp/note/note_list.html', context)

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {'note': note}
    return render(request, 'myapp/note/note_detail.html', context)