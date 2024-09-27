from rest_framework import viewsets
from .models import *
from .serializers import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


def create_user(request):
    # Логика создания пользователя
    user = CustomUser.objects.create(...)

    # Отправка уведомления через веб-сокеты
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications_group",
        {
            "type": "notification_message",
            "message": f"Новый пользователь {user.first_name} создан"
        }
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
