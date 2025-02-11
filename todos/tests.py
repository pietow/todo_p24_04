from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='First Todo',
            body='A body'
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'First Todo')
        self.assertEqual(Todo.objects.get(id=1).title, 'First Todo')
        self.assertEqual(self.todo.body, 'A body')
        self.assertEqual(str(self.todo), 'First Todo')

    def test_api_listview(self):
        response = self.client.get(
                    reverse('todo_list'),
        )
        self.assertEqual(response.status_code, 
                status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
        self.assertContains(response, "A body")

    def test_api_detailview(self):
        response = self.client.get(
            reverse(
                "todo_details", 
                kwargs={'pk': self.todo.id},
                )
        )
        self.assertEqual(response.status_code, 
                status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
        self.assertContains(response, "A body")


    



