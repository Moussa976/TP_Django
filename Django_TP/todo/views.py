from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_tasks = Task.objects.all
            messages.success(request,('La tâche a bien été ajoutée à la liste !'))
            return render(request, "todo/index.html", {"all_tasks":all_tasks})
    else:
        all_tasks = Task.objects.all
        return render(request,"todo/index.html",{"all_tasks":all_tasks})

def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    messages.success(request,('La tâche a bien été supprimée de la liste !'))
    return redirect('index')


def is_done(request, id):
    task = Task.objects.get(pk=id)
    task.is_done = True
    task.save()
    return redirect('index')

def not_done(request, id):
    task = Task.objects.get(pk=id)
    task.is_done = False
    task.save()
    return redirect('index')

def edit(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)

        form = TaskForm(request.POST or None, instance = task)

        if form.is_valid():
            form.save()
            messages.success(request,('La tâche a bien été modifiée !'))
            return redirect('index')
    else:
        task = Task.objects.get(pk=id)
        return render(request,"todo/edit.html",{"task":task})
