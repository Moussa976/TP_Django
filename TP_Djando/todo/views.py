from django.shortcuts import render, redirect  
from todo.forms import TaskForm  
from todo.models import Task 
# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = TaskForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('todo/index.html')  
            except:  
                pass 
    else:  
        form = TaskForm()  
    return render(request,'todo/add.html',{'form':form})  
def index(request):  
    tasks = Task.objects.all()  
    return render(request,"todo/index.html",{'tasks':tasks})  
def edit(request, id):  
    task = Task.objects.get(id=id)  
    return render(request,'todo/edit.html', {'task':task})  
def update(request, id):  
    task = Task.objects.get(id=id)  
    form = TaskForm(request.POST, instance = task)  
    if form.is_valid():  
        form.save()  
        return redirect("todo/index.html")  
    return render(request, 'todo/edit.html', {'task': task})  
def destroy(request, id):  
    task = Task.objects.get(id=id)  
    task.delete()  
    return redirect("todo/index.html")