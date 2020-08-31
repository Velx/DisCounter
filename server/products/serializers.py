from rest_framework import serializers
from .models import Products
from .tasks import check_price

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('api_id', 'name', 'price', 'current_price', 'image', 'ali_url')
        extra_kwargs = {
            'api_id': {
                'validators': [],
            }
        }

    def create(self, validated_data):
        product, created = Products.objects.get_or_create(**validated_data)
        product.save()
        user = self.context.get('user')
        product.products.add(user)
        return product

