from django.test import TestCase
from .models import Products
from .serializers import ProductSerializer


class TestProductModel(TestCase):
    def setUp(self) -> None:
        self.product = Products.objects.create(
            name='TEST',
            api_id="4000918899813",
            price=30345.77,
            current_price=30345.77,
            image="https://ae01.alicdn.com/kf/H94d5587dc2724f0e86bfe4a5cd759987R/DOOGEE-S95-Pro-8-256-IP68-IP69K.jpg",
            ali_url="https://aliexpress.ru/item/4000918899813.html"
        )

    def test_creation_success_name(self):
        assert self.product.name == 'TEST'

    def test_creation_success_api_id(self):
        assert self.product.api_id == "4000918899813"

    def test_creation_success_price(self):
        assert self.product.price == 30345.77

    def test_creation_success_current_price(self):
        assert self.product.current_price == 30345.77

    def test_creation_success_image(self):
        assert self.product.image == "https://ae01.alicdn.com/kf/H94d5587dc2724f0e86bfe4a5cd759987R/DOOGEE-S95-Pro-8-256-IP68-IP69K.jpg"

    def test_creation_success_ali_url(self):
        assert self.product.ali_url == "https://aliexpress.ru/item/4000918899813.html"


class TestProductsSerializer(TestCase):
    def setUp(self) -> None:
        self.product = Products.objects.create(
            name='TEST',
            api_id="4000918899813",
            price=30345.77,
            current_price=30345.77,
            image="https://ae01.alicdn.com/kf/H94d5587dc2724f0e86bfe4a5cd759987R/DOOGEE-S95-Pro-8-256-IP68-IP69K.jpg",
            ali_url="https://aliexpress.ru/item/4000918899813.html"
        )
        self.serializer = ProductSerializer(instance=self.product)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['api_id', 'name', 'price', 'current_price', 'image', 'ali_url'])

    def test_api_id_field_content(self):
        data = self.serializer.data
        assert data['api_id'] == self.product.api_id

    def test_name_field_content(self):
        data = self.serializer.data
        assert data['name'] == self.product.name

    def test_price_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['price'], str(self.product.price))

    def test_current_price_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['current_price'], str(self.product.current_price))

    def test_image_field_content(self):
        data = self.serializer.data
        assert data['image'] == self.product.image

    def test_ali_url_field_content(self):
        data = self.serializer.data
        assert data['ali_url'] == self.product.ali_url
