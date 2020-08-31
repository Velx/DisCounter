from unittest.mock import patch
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import authenticate
from django.core.cache import cache
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User, Token
from .serializers import UserSerializer
from .apiviews import UserViewSet, CustomAuthToken, ActivationView


class TestUserModel(TestCase):
    def setUp(self) -> None:
        user = User(username='TEST', email='test@gmail.com')
        user.set_password('testpassword')
        user.save()

    def test_creation_success_username(self):
        user = User.objects.get(username='TEST')
        self.assertTrue(isinstance(user, User))

    def test_creation_success_email(self):
        user = User.objects.get(email='test@gmail.com')
        self.assertTrue(isinstance(user, User))

    def test_creation_success_password(self):
        user = authenticate(username='TEST', password='testpassword')
        self.assertIsNotNone(user)

    def test_creation_success_token(self):
        user = User.objects.get(username='TEST')
        token = Token.objects.get(user=user)
        self.assertIsNotNone(token)


class TestUserSerializer(TestCase):
    def setUp(self) -> None:
        self.user = User(username='TEST2', email='test2@gmail.com')
        self.user.set_password('testpassword')
        self.user.save()
        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['username', 'email', 'products', 'e_notifications'])

    def test_username_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.user.username)

    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user.email)

    def test_e_notifications_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['e_notifications'], self.user.e_notifications)

    def test_products_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['products'], list(self.user.products.all()))


class TestCustomAuthTokenView(TestCase):
    def setUp(self) -> None:
        self.user = User(username='TEST2', email='test2@gmail.com')
        self.user.set_password('testpassword')
        self.user.save()

    def test_view(self):
        factory = APIRequestFactory()
        view = CustomAuthToken.as_view()
        request = factory.post('/api/login', {'username':'TEST2', 'password': 'testpassword'})
        response = view(request)
        self.assertEqual(response.status_code, 200)


class TestUserViewSet(TestCase):
    def setUp(self) -> None:
        self.user = User(username='TEST4', email='test4@gmail.com')
        self.user.set_password('testpassword')
        self.user.save()

    @staticmethod
    def create_in_serializer(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=User.objects.normalize_email(validated_data['email'])
        )
        user.set_password(validated_data['password'])
        token = 'ebcbf234-1688-43aa-b2d2-08a147e1d3ce'
        cache.set(token, user, timeout=259200)
        user.id = 0
        return user

    def create(self, request):
        serial = UserSerializer
        serial.create = TestUserViewSet.create_in_serializer
        serializer = serial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @patch.object(UserViewSet, 'create', create)
    def test_user_creation(self):
        factory = APIRequestFactory()
        view = UserViewSet.as_view({'post': 'create'})
        request = factory.post('/api/user', {'username': 'TEST3', 'password': 'testpassword',
                                             'email': 'test3@gmail.com'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_user_activation(self):
        factory = APIRequestFactory()
        view = ActivationView.as_view()
        request = factory.get('users/ebcbf234-1688-43aa-b2d2-08a147e1d3ce/activate')
        response = view(request, token='ebcbf234-1688-43aa-b2d2-08a147e1d3ce')
        self.assertEqual(response.status_code, 200)

    def test_user_retrieve(self):
        user = User.objects.get(username='TEST4')
        factory = APIRequestFactory()
        view = UserViewSet.as_view({'get': 'retrieve'})
        request = factory.get(f'users/{user.pk}')
        force_authenticate(request, user=user)
        response = view(request, pk=user.pk)
        self.assertEqual(user.username, response.data['username'])

    # def test_user_update(self):
    #     token = Token.objects.get(user=self.user)
    #     factory = APIRequestFactory()
    #     view = UserViewSet.as_view(actions={'PATCH': 'partial'})
    #     request = factory.patch('users/partial/', {'email': 'test5@gmail.com'},
    #                             content_type='application/json',
    #                             HTTP_AUTHORIZATION=f'Token {token}')
    #     force_authenticate(request, user=self.user, token=token)
    #     response = view(request)
    #     print(response)
    #     print(response.data)
    #     self.assertEqual(True, response)
