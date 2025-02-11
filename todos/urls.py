from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo, UpdateTodo, DeleteTodo

urlpatterns = [
    path("", ListTodo.as_view(), name="todo_list"),
    path("<int:pk>/",  DetailTodo.as_view(), name="todo_details"),
    path("create/",  CreateTodo.as_view(), name="todo_create"),
    path("update/<int:pk>/",  UpdateTodo.as_view(), name="todo_update"),
    path("delete/<int:pk>/",  DeleteTodo.as_view(), name="todo_delete"),

]