from django.shortcuts import render


def task_list(request):
    done_tasks = dict(
        task1=[{'task': 'Task 1', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task2=[{'task': 'Task 2', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task3=[{'task': 'Task 3', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task4=[{'task': 'Task 4', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],)

    headers = [
        'Task',
        'Created',
        'Due on',
        'Owner',
        'Mark'
    ]

    context = {
        'tasks': done_tasks,
        'headers': headers,
    }
    return render(request, 'todo_list.html', context=context)

def task_list_completed(request):
    completed_tasks = dict(
        task0=[{'task': 'Task 0', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": False}],)

    headers = [
        'Task',
        'Created',
        'Due on',
        'Owner',
        'Mark'
    ]

    context = {
        'headers': headers,
        'completed_tasks': completed_tasks
    }
    return render(request, 'completed_todo_list.html', context=context)