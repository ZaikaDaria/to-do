from django.urls import path
from .views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoUpdateStatusView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("todo_create/", TodoCreateView.as_view(), name="todo-create"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="todo-update"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo-delete"),
    path("todo_update_status/<int:pk>/", TodoUpdateStatusView.as_view(), name="todo-update-status"),
    path("tag_list/", TagListView.as_view(), name="tag-list"),
    path("tag_create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "todo"
