from rest_framework import serializers

from appStoreV2.models.sale import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
        # fields = ['name', 'price', 'inventory']
