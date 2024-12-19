from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Career
from .serializers import CareerSerializer, CareerListSerializer

# Create your views here.
class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CareerSerializer
        return CareerListSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.title = request.data.get('title', instance.title)
        instance.content = request.data.get('content', instance.content)
        serializer = self.get_serializer(instance, data={
            'title': instance.title, 
            'content': instance.content
        }, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
