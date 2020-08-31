from uuid import uuid4
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from .tasks import send_activation_code
from django.core.cache import cache


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'e_notifications': user.e_notifications
        })


class ActivationView(APIView):
    def get(self, request, token):
        user = cache.get(token)
        if user:
            user.save()
            cache.delete_pattern(token)
            return Response({"message": "Created"}, status=200)
        else:
            return Response({"message": "Your activation token is expired"}, status=404)


class PasswordResetView(APIView):
    def post(self, request):
        if not request.data.get('email'):
            return Response({"message": "Please include email into your request"}, status=400)
        email = User.objects.normalize_email(request.data.get('email'))
        user = get_object_or_404(User, email=email)
        token = uuid4()
        cache.set(token, user, timeout=259200)
        send_activation_code.delay(
            subject='Reset password request',
            to_email=user.email,
            activation_code=token,
            action='password-reset',
            template='users/password_reset_email.html'
        )
        return Response(status=200)


class PasswordResetTokenView(APIView):
    def get(self, request, token):
        user = cache.get(token)
        if user:
            return Response(status=200)
        else:
            return Response({"message": "Your activation token is expired"}, status=404)

    def post(self, request, token):
        user = cache.get(token)
        if user is None:
            return Response({"message": "Your activation token is expired"}, status=404)
        else:
            if not request.data.get('password'):
                return Response({"message": "Please include password into your request"}, status=400)
            user.set_password(request.data['password'])
            user.save()
            cache.delete_pattern(token)
            return Response({"message": "Created"}, status=200)


class UserViewSet(viewsets.ViewSet):

    def get_queryset(self):
        user_pk = self.request.user.pk
        return User.objects.filter(pk=user_pk)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [DjangoModelPermissions]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=['PATCH'])
    def partial(self, request):
        data = {}
        for item in request.data:
            if request.data[item] is not None:
                data[item] = request.data[item]
        serializer = UserSerializer(request.user, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)