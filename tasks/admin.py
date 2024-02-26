from django.contrib import admin
from .models import TaskGroup, Task

# Register your models here.

class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup

class TaskAdmin(admin.ModelAdmin):
    model = Task

    list_display = ['name', 'due_date']

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)