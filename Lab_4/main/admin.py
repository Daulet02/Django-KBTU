from django.contrib import admin

# Register your models here.
from main.models import Todo_list, Task


@admin.register(Todo_list)
class Todo_list_admin(admin.ModelAdmin):
    list_display = ['list_name']


@admin.register(Task)
class Task_admin(admin.ModelAdmin):
    list_display = ['task_name', 'created', 'due_on', 'owner', 'todo_list']