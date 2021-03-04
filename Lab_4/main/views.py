from django.shortcuts import render

# Create your views here.
from main.models import Todo_list, Task

def main_page(request):
    return render(request, 'index.html')

def todo_list(request, pk):
    todo = Todo_list.objects.get(id=pk)
    tasks = Task.objects.filter(completed=False)
    context = {
        "todo": todo,
        "tasks": tasks,
        "completed": False
    }
    return render(request, 'todo_list.html', context=context)


def todo_list_completed(request, pk):
    todo = Todo_list.objects.get(id=pk)
    tasks = Task.objects.filter(completed=True)
    context = {
        "todo": todo,
        "tasks": tasks,
        "completed": True
    }
    return render(request, 'completed_todo_list.html', context=context)