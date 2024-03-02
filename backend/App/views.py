from django.shortcuts import get_object_or_404, redirect, render
from App.models import Task
from App.forms import TaskForm

# Create your views here.


def Index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "tasks": tasks,
        "form": form,
    }
    return render(request, "index.html", context)


def Detail_task(request, slug):
    task = get_object_or_404(Task, Slug=slug)
    context = {
        "task": task
    }
    return render(request, "task.html", context)


def Update_task(request, slug):
    task = get_object_or_404(Task, Slug=slug)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("detail" ,slug = task.Slug)

    context = {
        "form": form
    }
    return render(request, "task.html", context)


def Delete_task(request, slug):
    task = get_object_or_404(Task, Slug=slug)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    context = {
        "task": task
    }
    return render(request, "delete_task.html", context)
