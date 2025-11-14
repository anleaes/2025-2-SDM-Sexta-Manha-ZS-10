from django.db import models

# Create your models here.
class Localizacao(models.Model):
    cidade = models.CharField('Cidade', max_length=50)
    estado = models.CharField('Estado', max_length=50)
    pais = models.CharField('País', max_length=50)
    cep = models.CharField('CEP', max_length=20)