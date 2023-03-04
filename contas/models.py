from django.db import models
from django.conf import settings


class Contas(models.Model):
    nome = models.CharField(max_length=100)
    operacao = models.CharField(
        max_length=2,
        choices=(
            ('SI', 'Simples'),
            ('RA', 'Rateio'),
        )
    )
    situacao = models.CharField(max_length=1, default='A')

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'