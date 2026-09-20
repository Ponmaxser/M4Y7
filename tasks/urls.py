from django.urls import path

from .views import TaskCreateView, TaskDetailView, TaskListView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-uprate"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete")
]

app_name = "tasks"