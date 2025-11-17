from rest_framework import viewsets
from .models import Hospedagem
from .serializer import HospedagemSerializer

# Create your views here.
class HospedagemViewSet(viewsets.ModelViewSet):
    queryset = Hospedagem.objects.all()
    serializer_class = HospedagemSerializer