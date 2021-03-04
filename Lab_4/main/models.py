from django.conf import settings
from django.db import models


# Create your models here.
class Todo_list(models.Model):
    list_name = models.CharField(max_length=200)

    def __str__(self):
        return self.list_name


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    due_on = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(Todo_list, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
