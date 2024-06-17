from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import get_object_or_404, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from selfstudy.models import TestMaterial
from selfstudy.serializers import TestSerializer


class TestMaterialListAPIView(ListAPIView):
    """Контроллер для отображения списка тестов."""

    serializer_class = TestSerializer
    queryset = TestMaterial.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ('material',)
    ordering_fields = ('material',)
    search_fields = ('question',)


class TestMaterialRetrieveAPIView(RetrieveAPIView):
    """Контроллер для отображения одного теста."""

    serializer_class = TestSerializer
    queryset = TestMaterial.objects.all()


class TestAPIView(APIView):
    """Контроллер для проверки ответа на вопрос теста.
    На вход получает json в формате: {"id": id, "answer": "ответ"}."""

    def post(self, request):

        test_id = request.data.get('id')
        user_answer = request.data.get('answer')

        test_object = get_object_or_404(TestMaterial, pk=test_id)

        if test_object.answer == user_answer:
            return JsonResponse({"result": True}, status=200)
        return JsonResponse({"result": False}, status=200)
