from rest_framework.response import Response
from rest_framework.views import APIView
from appStoreV2.models.product import Product
from appStoreV2.serializer.productSerializer import ProductSerializer

class ProductAPIView(APIView):

    def get(self,request):
        #traigo todos los valores (Productos)
        products = Product.objects.all()
        #Se pasa la consulta, es decir serializa una instancia (many=True para que sepa que es un listado)
        products_serializer = ProductSerializer(products, many = True)
        return Response(products_serializer.data)