from django.urls import path
from .views import index, task_list, task_detail, TaskListView

urlpatterns = [
    path('', index, name='index'),
    path('list', TaskListView.as_view(), name='list'),
    path('<int:pk>/detail', task_detail, name='task-detail'),
]

app_name = 'tasks'