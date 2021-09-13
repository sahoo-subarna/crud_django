from django.shortcuts import redirect, render

from . models import Task
from . forms import TaskForm
# Create your views here.


def home(request): #READ
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks": tasks})


def add_new_task(request): #CREATE
    if request.method == "POST":
        form = TaskForm(request.POST)
        form.save()
        return redirect("home")

    else:
        task_form = TaskForm()
        return render(request, "add_new_task.html", {"task_form": task_form})


def update_task(request, id): #UPDATE
    if request.method == "POST":
        instance = Task.objects.get(pk=id)
        form = TaskForm(request.POST, instance=instance)
        form.save()
        return redirect("home")

    else: #GET
        task = Task.objects.get(pk=id)
        form = TaskForm(instance= task)
        return render(request,"add_new_task.html", {"task_form": form })


def delete_task(request, id): #DELETE
    Task.objects.get(pk=id).delete()
    return redirect("/")