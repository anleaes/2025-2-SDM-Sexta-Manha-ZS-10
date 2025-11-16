from django.db import models

# Create your models here.
class Pagamento(models.Model):
    valor = models.FloatField('Valor')
    metodo_pagamento = models.CharField('Método de Pagamento', max_length=50)
    status_pagamento = models.CharField('Status do Pagamento', max_length=50)
    data_pagamento = models.DateField('Data do Pagamento')