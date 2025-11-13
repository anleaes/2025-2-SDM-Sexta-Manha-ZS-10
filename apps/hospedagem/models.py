from django.db import models

# Modelo criado conforme o diagrama de classes
class Hospedagem(models.Model):
    nome = models.CharField('Nome', max_length=70)
    descricao = models.TextField('Descrição', max_length=500)
    preco_diaria = models.FloatField('Preço da Diária')
    disponivel = models.BooleanField('Disponível', default=True)

    class Meta:
        verbose_name = 'Hospedagem'
        verbose_name_plural = 'Hospedagens'
        ordering = ['id']

    def __str__(self):
        return self.nome