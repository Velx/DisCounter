from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Products


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    e_notifications = models.BooleanField(default=False)
    products = models.ManyToManyField(Products, related_name='products', blank=True)
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)