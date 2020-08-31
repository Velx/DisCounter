from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .apiviews import ActivationView, UserViewSet


urlpatterns = [
    path('login', views.obtain_auth_token),
    path('users/<uuid:token>/activate', ActivationView.as_view(), name='activation'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns += router.urls