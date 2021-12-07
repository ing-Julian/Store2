# from rest_framework.response import Response
# from rest_framework.views import APIView
# from appStoreV2.models.product import Product
# from appStoreV2.serializer.productSerializer import ProductSerializer

# class ProductAPIView(APIView):

#     def get(self,request):
#         #traigo todos los valores (Productos)
#         products = Product.objects.all()
#         #Se pasa la consulta, es decir serializa una instancia (many=True para que sepa que es un listado)
#         products_serializer = ProductSerializer(products, many = True)
#         return Response(products_serializer.data)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from appStoreV2.models.product import Product
from appStoreV2.serializer.productSerializer import ProductSerializer

@api_view(['GET', 'POST'])
def product_api_view(request):

    # List
    if request.method == 'GET':
        #traigo todos los valores (Productos)
        products = Product.objects.all()
        #Se pasa la consulta, es decir serializa una instancia (many=True para que sepa que es un listado)
        products_serializer = ProductSerializer(products, many = True)
        return Response(products_serializer.data, status = status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':
        print(request.data)
        #deserializa la información, y compara con un objeto, para validar
        product_serializer = ProductSerializer(data = request.data)
        #Valida si cumple con el formato de nuestro modelo
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status = status.HTTP_201_CREATED)
        return Response(product_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request,pk=None):
    #queryset
    product = Product.objects.filter(id = pk).first() # variable que guarda la instancia del usuario
    #Validate
    if product:
        # retrive
        if request.method == 'GET':
            product_serializer= ProductSerializer(product)
            return Response(product_serializer.data, status = status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            product_serializer = ProductSerializer(product, data = request.data)  # data es La información que se pasa desde el navegador, y asi se entiende actualización por el put ...
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status = status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        #DELETE
        elif request.method == 'DELETE':
            product.delete()
            return Response({'mesage': 'Producto Eliminado correctamente'}, status.HTTP_200_OK)

        return Response({'message': 'No se ha encontrado producto con estos datos'}, status= status.HTTP_400_BAD_REQUEST)