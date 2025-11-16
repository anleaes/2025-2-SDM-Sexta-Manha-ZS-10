from rest_framework import viewsets
from .models import Anfitriao
from .serializer import AnfitriaoSerializer

# Create your views here.
class AnfitriaoViewSet(viewsets.ModelViewSet):
    queryset = Anfitriao.objects.all()
    serializer_class = AnfitriaoSerializer