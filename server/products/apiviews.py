from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Products
from users.models import User
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

from .tasks import check_price

class ProductsViewSet(viewsets.ViewSet):

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        if request.user.is_authenticated:
            queryset = request.user.products.all()
        else:
            queryset = Products.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = request.user.products.all()
        product = get_object_or_404(queryset, api_id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = request.user.products.all()
        product = get_object_or_404(queryset, api_id=pk)
        serializer = ProductSerializer(product)
        self.preform_delete(product)
        return Response({}, status=status.HTTP_200_OK)

    def create(self, request,):
        api_id, title, image, normal_price, current_price = check_price(request.data['ali_url'])
        data = {
            'api_id': api_id,
            'name': title,
            'price': normal_price,
            'current_price': current_price,
            'image': image,
            'ali_url': request.data['ali_url']
        }
        serializer = ProductSerializer(data=data, context={
            'user': request.user
        })
        if serializer.is_valid():
            self.preform_create(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def preform_delete(self, instance):
        self.request.user.products.remove(instance)

    def preform_create(self, serializer):
        serializer.create(serializer.validated_data)
