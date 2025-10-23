from django.http import HttpResponse
from django.template import loader


class Note:
    def __init__(self, text):
        self.note_text = text

notes_list = [Note('note_text_1'), Note('note_text_2'), Note('note_text_3')]

def index(request):
    # return HttpResponse("Hello from Notes app.")
    template = loader.get_template("notes/index.html")
    context = {"notes_list": notes_list}
    return HttpResponse(template.render(context, request))