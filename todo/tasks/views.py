from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import context

from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    task_list = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        print('The data is ' , request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'task_list': task_list, 'form': form}
    return render(request, 'tasks/list.html', context)

def update(request, task_id):
    task = Task.objects.get(pk=task_id)
    #print(task.status)
    task.status = not(task.status)
    task.save()
    return redirect('/')

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('/')
    