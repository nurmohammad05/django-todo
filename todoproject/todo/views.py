from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect("task_list")
    return render(request, "todo/task_list.html", {"tasks": tasks})

def task_delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect("task_list")

def task_toggle(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")
