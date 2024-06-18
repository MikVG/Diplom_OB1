from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from selfstudy.models import TestMaterial, Chapter, Material
from users.models import User


class TestMaterialTestCase(APITestCase):
    """Класс тест кейсов для тестирования контроллеров модели TestMaterial."""

    def setUp(self):
        """Метод описывающий данные для тестов."""
        self.user = User.objects.create(email="test@test.ru", password="12345")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.chapter = Chapter.objects.create(title='python', description='python')
        self.material = Material.objects.create(title='операторы', description='операторы', chapter=self.chapter)
        self.test_material = TestMaterial.objects.create(material=self.material, question='какой язык вы учите?',
                                                         answer='python')

    def test_testmaterail_list(self):
        """Метод для тестирования списка материалов."""

        url = reverse("selfstudy:test_list")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.test_material.pk,
                "material": self.test_material.material.pk,
                "question": "какой язык вы учите?"
            },
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_testmaterial_retrieve(self):
        """Метод для тестирования одного материала."""

        url = reverse("selfstudy:test_detail", args=(self.test_material.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("question"), self.test_material.question)

    def test_testmaterial_answer_true(self):
        """Метод для тестирования правильного ответа на вопрос теста."""

        url = reverse("selfstudy:test")
        data = {
                "id": self.test_material.pk,
                "answer": "python"
            }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_testmaterial_answer_false(self):
        """Метод для тестирования неправильного ответа на вопрос теста."""

        url = reverse("selfstudy:test")
        data = {
                "id": self.test_material.pk,
                "answer": "golang"
            }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_testmaterial_answer_404(self):
        """Метод для тестирования отправки ответа на несуществующий вопрос теста."""

        url = reverse("selfstudy:test")
        data = {
                "id": 5,
                "answer": "python"
            }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
