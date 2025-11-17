from django.db import models
from apps.pagamentos.models import Pagamento
from clientes.models import Cliente
from hospedagens.models import Hospedagem

# Create your models here.
class Reserva(models.Model):
    data_checkin = models.DateField('Data de Check-in')
    data_checkout = models.DateField('Data de Check-out')
    quantidade_hospedes = models.IntegerField('Quantidade de Hóspedes')
    valor_total = models.FloatField('Valor Total')

    # Foreign Keys
    pagamento = models.ManyToManyField(Pagamento)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return f'Reserva #{self.id} - {self.cliente.nome}'