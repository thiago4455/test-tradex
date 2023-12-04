from rest_framework import serializers
from api.models import Product, Price

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        price = Price.objects.filter(product=obj).order_by('-created_at').first()
        if price:
            return price.price
        return None

    class Meta:
        model = Product
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'