from django import forms

from .models import Task, TaskGroup


class TaskForm(forms.Form):
    name = forms.CharField(label="Task Date", max_length = 100)
    due_date = forms.DateTimeField(label="Due Date", required=True)
    taskgroup = forms.ModelChoiceField(queryset=TaskGroup.objects.all())

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'