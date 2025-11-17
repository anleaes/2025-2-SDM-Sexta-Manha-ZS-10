from django.db import models
from categorias.models import Categoria
from localizacoes.models import Localizacao
from anfitrioes.models import Anfitriao

# Create your models here.
class Hospedagem(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=200)
    preco_diaria = models.FloatField('Preço da Diária')
    disponivel = models.BooleanField('Disponível', default=True)

    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    anfitriao = models.ForeignKey(Anfitriao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Hospedagem'
        verbose_name_plural = 'Hospedagens'
        ordering = ['id']

    def __str__(self):
        return self.nome