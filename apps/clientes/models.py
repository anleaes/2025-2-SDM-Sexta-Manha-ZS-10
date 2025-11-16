from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    data_cadastro = models.DateField('Data de Cadastro')