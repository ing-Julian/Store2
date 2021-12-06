from rest_framework import serializers

from appStoreV2.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price', 'inventory']
