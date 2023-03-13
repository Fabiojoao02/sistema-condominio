from django.db import models
from django.conf import settings
from contas.models import Contas
from condominio.models import Morador


class Calculos(models.Model):
    anomes = models.CharField(max_length=6)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    conta = models.ForeignKey(Contas, on_delete=models.CASCADE)
    valor = models.FloatField(default=0)
    tipo_calculo = models.CharField(
        max_length=3,
        choices=(
            ('SIM', 'Simples'),
            ('RAT', 'Rateio'),
            ('RAA', 'Rateio Água'),
            ('RAG', 'Rateio Gás'),
        )
    )

    def __str__(self) -> str:
        return self.anomes

    class Meta:
        verbose_name = 'Calculo'
        verbose_name_plural = 'Calculos'
