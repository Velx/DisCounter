from django.core.cache import cache
from rest_framework import serializers
from users.models import User
from .tasks import send_activation_code

from products.serializers import ProductSerializer

from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'products', 'e_notifications')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    products = ProductSerializer(many=True, read_only=True)

    def create(self, validated_data, token_generator=uuid4):

        user = User(
            username=validated_data['username'],
            email=User.objects.normalize_email(validated_data['email'])
        )
        user.set_password(validated_data['password'])
        token = token_generator()
        cache.set(token, user, timeout=259200)
        user.id = 0
        send_activation_code.delay(
            subject='Activate your account',
            to_email=user.email,
            activation_code=token,
            action='activation',
            template='users/activation_email.html'
        )
        return user

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        if validated_data.get('email'):
            instance.email = User.objects.normalize_email(validated_data['email'])
        if 'e_notifications' in validated_data:
            instance.e_notifications = validated_data['e_notifications']
        instance.save()
        return instance
