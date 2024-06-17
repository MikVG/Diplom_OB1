from rest_framework.serializers import ModelSerializer
from selfstudy.models import TestMaterial


class TestSerializer(ModelSerializer):
    """Сериализатор для контроллеров списка тестов и одного теста."""

    class Meta:
        model = TestMaterial
        fields = ('id', 'material', 'question')
