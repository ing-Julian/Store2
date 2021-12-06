from rest_framework.response import Response
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
        return Response(clients_serializer.data)

    elif request.method == 'POST':
        print(request.data)