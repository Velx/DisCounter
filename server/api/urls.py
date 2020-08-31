from django.urls import path
from rest_framework.routers import DefaultRouter
from users.apiviews import ActivationView, UserViewSet, PasswordResetView, PasswordResetTokenView, CustomAuthToken
from products.apiviews import ProductsViewSet
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('users/<uuid:token>/activate', ActivationView.as_view(), name='activation'),
    path('password-reset', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/<uuid:token>', PasswordResetTokenView.as_view(), name='password reset token'),
    path('notification-token/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductsViewSet, basename='products')
urlpatterns += router.urls