from django.db import models
from django.conf import settings
from django.contrib import admin
from contas.models import Contas
from condominio.models import Morador


class Leituras(models.Model):
    mesano = models.CharField(max_length=6)
    conta = models.ForeignKey(Contas, on_delete=models.CASCADE)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    leitura_inical = models.FloatField(default=0)
    leitura_final = models.FloatField(default=0)
    data_leitura = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.mesano

    class Meta:
        verbose_name = 'Leitura'
        verbose_name_plural = 'Leituras'
