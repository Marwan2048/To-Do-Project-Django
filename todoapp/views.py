from django.shortcuts import render ,redirect
from .models import Task
from .forms import TaskForm

def home(request):
    while True:
        tasks = Task.objects.filter(completed = False)
        q = tasks.count()
        if q != 0:
            return render(request, 'home.html',{"tasks":tasks})
        else:
            return render(request,'home_no_tasks.html')

    
def add_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add_task.html',{"form":form})


def completed_task(request):
    tasks = Task.objects.filter(completed = True)
    if tasks.count() > 0:
        return render(request,'completed_task.html',{"tasks":tasks})
    elif tasks.count() == 0:
        return render(request,'completed_no_tasks.html')

def mark_as_done(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.completed = True
    tasks.save()
    return redirect('home')

def update_task(request,pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST ,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update_task.html',{"form":form})


def delete_task(request , pk):
    task = Task.objects.get(id = pk)
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request , 'delete_task.html' ,{"task":task})
