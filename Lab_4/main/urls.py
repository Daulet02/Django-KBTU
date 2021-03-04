from django.urls import path

from main.views import *

urlpatterns = [
    path('', main_page),
    path('<int:pk>', todo_list),
    path('<int:pk>/completed/', todo_list_completed)
]