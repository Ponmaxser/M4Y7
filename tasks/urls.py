from django.urls import path

from .views import TaskCreateView, TaskDetailView, TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create")
]

app_name = "tasks"