from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Сериализатор для работы с контроллером создания пользователя."""

    class Meta:
        model = User
        fields = '__all__'
