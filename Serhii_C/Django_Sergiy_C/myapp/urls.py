# # myapp/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path("<int:question_id>/", views.note1, name="note1"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.note2, name="note2"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.note3, name="note3"),
# ]

# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='list'),
    path('<int:pk>/', views.note_detail, name='detail'), 
]