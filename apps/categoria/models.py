from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=100)
    ativo = models.BooleanField('Ativo', default=True)
    limite_hospedes = models.IntegerField('Limite de Hóspedes', default=1)