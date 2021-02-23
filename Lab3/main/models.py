from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=100)
    created = models.CharField(max_length=100)
    due_on = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    mark = models.BooleanField(default=True)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'