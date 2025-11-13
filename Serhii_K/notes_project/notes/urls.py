from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path("", views.index, name="index"),
    # path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.detail_note, name="detail_note"),
    # path("<int:pk>/", views.DetailView.as_view(), name="note_detail"),
    path("add_note/", views.add_note, name="add_note"),
    path("<int:note_id>/edit/", views.edit_note, name="edit_note"),
    path("<int:note_id>/delete/", views.delete_note, name="delete_note"),
]