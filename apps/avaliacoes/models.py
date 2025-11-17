from django.db import models
from clientes.models import Cliente
from hospedagens.models import Hospedagem

# Create your models here.
class Avaliacao(models.Model):
    nota = models.IntegerField('Nota')
    comentario = models.TextField('Comentário', max_length=200)
    data_avaliacao = models.DateField('Data da Avaliação', auto_now_add=True)
    publicada = models.BooleanField('Publicada', default=False)

    autor = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['id']

    def __str__(self):
        return f"Avaliação: {self.nota} - {self.autor.nome} - {self.comentario}"