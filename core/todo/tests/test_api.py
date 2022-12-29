from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from todo.models import Task
import pytest

User = get_user_model()


@pytest.fixture
def temp_user():
    user = User.objects.create(email="test@gmail.com", password="T@123456")
    return user


@pytest.fixture
def temp_task(temp_user):
    task = Task.objects.create(author=temp_user, title="test_pk_user")
    return task


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_401_status(self):
        url = reverse("todo:api-v1:task-list")
        client = APIClient()
        response = client.get(url)
        assert response.status_code == 401

    def test_get_task_response_200_status(self, temp_user):
        url = reverse("todo:api-v1:task-list")
        client = APIClient()
        client.force_authenticate(user=temp_user)
        response = client.get(url)
        assert response.status_code == 200

    def test_get_one_task_response_200_status(self, temp_user, temp_task):
        url = reverse("todo:api-v1:task-list")
        url = url + f"{temp_task.pk}/"
        client = APIClient()
        client.force_authenticate(user=temp_user)
        response = client.get(url)
        assert response.status_code == 200
        assert response.data.get("title") == temp_task.title
    
    def test_put_one_task_response_200_status(self, temp_user, temp_task):
        url = reverse("todo:api-v1:task-list")
        url = url + f"{temp_task.pk}/"
        client = APIClient()
        client.force_authenticate(user=temp_user)
        dela = {
            "title":"test_put"
        }
        response = client.put(url,data=dela)
        assert response.status_code == 200
        assert response.data.get("title") == dela.get("title")

    def test_create_task_response_201_status(self, temp_user):
        url = reverse("todo:api-v1:task-list")
        client = APIClient()
        client.force_authenticate(user=temp_user)
        data = {
            "title": "test1",
            "status": True
        }
        response = client.post(url, data=data)
        assert response.status_code == 201
