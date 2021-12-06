from rest_framework import serializers

from appStoreV2.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ['name', 'price', 'inventory']
