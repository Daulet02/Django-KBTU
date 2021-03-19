from django.contrib import admin
from main.models import TodoList, Task

admin.site.register(TodoList)
admin.site.register(Task)