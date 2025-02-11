from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Todo
from .serializers import TodoSerializer

class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodo(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer