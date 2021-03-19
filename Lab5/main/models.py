from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']



class Task(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    due_to = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['id']