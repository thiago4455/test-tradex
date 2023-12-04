from django.test import TestCase, Client
from rest_framework import status
from .models import Product, Price
from .serializers import ProductSerializer, PriceSerializer
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductViewSetTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Create a product object
        self.product = Product.objects.create(
            name="Test Product",
            ean="1234567890123",
            image="imagens/1701647295.png",
            min_price=10.00,
            max_price=20.00
        )

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized product is included in the response
        products = response.data
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]['name'], self.product.name)
        self.assertEqual(products[0]['ean'], self.product.ean)

    def test_create_product(self):
        data = {
            "name": "New Product",
            "ean": "9876543210987",
            "min_price": 15.00,
            "max_price": 25.00
        }

        response = self.client.post('/api/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the product was created in the database
        product = Product.objects.get(ean=data['ean'])
        self.assertEqual(product.name, data['name'])
        self.assertEqual(product.ean, data['ean'])

    def test_retrieve_product(self):
        response = self.client.get('/api/products/{}/'.format(self.product.ean))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized product is included in the response
        product = response.data
        self.assertEqual(product['name'], self.product.name)
        self.assertEqual(product['ean'], self.product.ean)