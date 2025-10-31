

from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='list'),
    path('<int:pk>/', views.note_detail, name='detail'),
    path('create/', views.note_create, name='create'),
    path('notes/<int:pk>/update/', views.note_update, name='update'),
    path('notes/<int:pk>/delete/', views.note_delete, name='delete'),
    path('category/create/', views.create_category, name='create_category')
]