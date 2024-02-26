from datetime import datetime
from django.db import models
from django.urls import reverse

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey('TaskGroup', 
                                  on_delete=models.CASCADE, 
                                  related_name='tasks')
    
    def __str__(self):
        # private method
        return '{} due on {}'.format(self.name, self.due_date)
    
    def get_absolute_url(self):
        return reverse('tasks:task-detail', args=[self.pk])
    
    @property
    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date']
        unique_together = ['due_date', 'name']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    # purpose of task-detail so I can refer to as a string in path('', include='')
    # path('/task/<int:pk>')

# Create your models here.
