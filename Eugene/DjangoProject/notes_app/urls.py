from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='index'),
    path('create/', views.NoteCreateView.as_view(), name='create_note'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]