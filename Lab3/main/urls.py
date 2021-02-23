from django.urls import path
from . import views
from main.views import task_list, task_list_completed

urlpatterns = [
    path('todos/', task_list),
    path('todos/1/completed', task_list_completed)
]