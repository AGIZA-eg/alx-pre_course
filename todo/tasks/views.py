from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def index(request):
    task = Task.objects.all()

    if request.method == 'POST':
        new_task = Task(
            title = request.POST['title']
        )
        new_task.save()
        return redirect('/')

    return render(request,"index.html",{'tasks': task})
def delete(request, pk):
    todo=Task.objects.get(id=pk)
    todo.delete()
    return redirect('/')
