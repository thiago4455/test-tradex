from rest_framework import viewsets, generics
from api.models import Product, Price
from api.serializers import ProductSerializer, PriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for Products.

    General ViewSet description

    list: List all Products

    retrieve: Retrieve a specific Product

    update: Update a Product

    create: Create a Product

    partial_update: Patch a Product

    destroy: Delete a Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer