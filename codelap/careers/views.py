from rest_framework import viewsets

from .models import Career
from .serializers import CareerSerializer

# Create your views here.
class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer