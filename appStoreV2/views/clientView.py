from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from appStoreV2.models.client import Client
from appStoreV2.serializer.clientSerializer import ClientSerializer

@api_view(['GET', 'POST'])
def client_api_view(request):

    if request.method == 'GET':
        #traigo todos los valores (Productos)
        clients = Client.objects.all()
        #Se pasa la consulta, es decir serializa una instancia (many=True para que sepa que es un listado)
        clients_serializer = ClientSerializer(clients, many = True)
        return Response(clients_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        print(request.data)
        #deserializa la información, y compara con un objeto, para validar
        client_serializer = ClientSerializer(data = request.data)
        #Valida si cumple con el formato de nuestro modelo
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data, status = status.HTTP_201_CREATED)
        return Response(client_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail_view(request,pk=None):

    if request.method == 'GET':
        client = Client.objects.filter(id = pk).first()
        client_serializer= ClientSerializer(client)
        return Response(client_serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        client = Client.objects.filter(id = pk).first() # variable que guarda la instancia del usuario
        client_serializer = ClientSerializer(client, data = request.data)  # data es La información que se pasa desde el navegador, y asi se entiende actualización por el put ...
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data, status = status.HTTP_200_OK)
        return Response(client_serializer.errors)

    elif request.method == 'DELETE':
        client = Client.objects.filter(id = pk).first() 
        client.delete()
        return Response('Cliente Eliminado')