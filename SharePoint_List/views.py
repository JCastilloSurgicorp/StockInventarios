from rest_framework.views import APIView
from rest_framework.response import Response
from .service import get_list_items, update_list_item
from .serializers import *

class SharePointListView(APIView):
    def get(self, request, list_title):
        items = get_list_items(list_title)
        serializer = SharePointItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, list_title):
        # Crear nuevo item
        # Implementar lógica similar a update_list_item
        return Response(status=201)

class SharePointItemDetailView(APIView):
    def get(self, request, list_title, item_id):
        items = get_list_items(list_title)
        item = next((i for i in items if i.id == item_id), None)
        if not item:
            return Response(status=404)
        serializer = SharePointItemSerializer(item)
        return Response(serializer.data)
    
    def put(self, request, list_title, item_id):
        success = update_list_item(list_title, item_id, request.data)
        return Response(status=200 if success else 400)
    
    def delete(self, request, list_title, item_id):
        # Implementar eliminación
        return Response(status=204)
                        