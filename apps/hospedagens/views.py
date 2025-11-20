from rest_framework import viewsets
from .models import Hospedagem
from .serializer import HospedagemSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class HospedagemViewSet(viewsets.ModelViewSet):
    queryset = Hospedagem.objects.all()
    serializer_class = HospedagemSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria', 'localizacao', 'disponivel']