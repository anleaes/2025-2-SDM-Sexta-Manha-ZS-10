from rest_framework import viewsets
from .models import Localizacao
from .serializer import LocalizacaoSerializer

# Create your views here.
class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer