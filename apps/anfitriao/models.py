from django.db import models

# Create your models here.
class Anfitriao(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=80)
    telefone = models.CharField('Telefone', max_length=20)
    avaliacao_media = models.FloatField('Avaliação Média', default=0.0)
    
    class Meta:
        verbose_name = 'Anfitrião'
        verbose_name_plural = 'Anfitriões'
        ordering = ['id']

    def __str__(self):
        return self.nome