from django.contrib import admin
from appStoreV2.models.product import Product
from appStoreV2.models.bill import Bill
from appStoreV2.models.client import Client
from appStoreV2.models.sale import Sale


# Register your models here.

admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Client)
admin.site.register(Sale)
