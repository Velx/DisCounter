from django.contrib import admin
from .models import Products


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Products, ProductAdmin)
