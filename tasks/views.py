from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def task_list(request):
    tasks = Task.objects.all()
    ctx = {
        "tasks": tasks
    }

    return render(request, 'task_list.html', ctx)

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    ctx = { 'task': task }

    return render(request, 'task_detail.html'. ctx)

class TaskListView(ListView):
    model = Task
    tempalte_name = 'task_list.html'

class TaskDetailView(DetailView):
    model = Task
    tempalte_name = 'task_detail.html'