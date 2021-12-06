from rest_framework import serializers

from appStoreV2.models.bill import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        # fields = ['name', 'price', 'inventory']
