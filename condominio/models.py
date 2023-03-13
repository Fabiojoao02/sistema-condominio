import os
from PIL import Image
from django.db import models
from django.conf import settings
from django.forms import ValidationError

import re
from utils.validacpf import valida_cpf


class Condominio(models.Model):
    nome = models.CharField(max_length=255)
    Endereco = models.CharField(max_length=255)
    Cidade = models.CharField(max_length=100)
    Bairro = models.CharField(max_length=100)
    CEP = models.CharField(max_length=8)
    Estado = models.CharField(
        max_length=2,
        default='SC',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    Fracao_ideal_tem = models.CharField(
        max_length=1,
        choices=(
            ('S', 'Sim'),
            ('N', 'Não'),
        )

    )
    Foto = models.ImageField(
        upload_to='condominio_imagens', blank=True, null=True)
    mostrar = models.BooleanField(default=True)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close
            return
        new_width = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_width), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        # print('Imagem foi redimencionada.')
        # print(img_full_path)

    def save(self, *args, **kwargs) -> None:
        return super().save(*args, **kwargs)

        max_image_size = 800

        if self.Foto:
            self.resize_image(self.Foto, max_image_size)

    def __str__(self) -> str:
        return self.nome

    def clean(self):
        error_messages = {}

        if re.search(r'[^0-9]', self.CEP) or len(self.CEP) < 8:
            error_messages['CEP'] = 'CEP inválido, digite apenas números 8 dígitos'

        if error_messages:
            raise ValidationError(error_messages)


class Bloco(models.Model):
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    situacao = models.CharField(max_length=1, default='A', editable=False)
    Taxa_condominio = models.FloatField(default=0)
    Fundo_reserva = models.FloatField(default=0)

    def get_Taxa_condominio(self):
        return f' {self.Taxa_condominio:.2f}%'.replace('.', ',')
    get_Taxa_condominio.short_description = 'Tx Condominio'

    def get_Fundo_reserva(self):
        return f' {self.Fundo_reserva:.2f}%'.replace('.', ',')
    get_Fundo_reserva.short_description = 'Fundo Reserva'

    def __str__(self) -> str:
        return self.nome or self.condominio.nome

    class Meta:
        verbose_name = 'Bloco'
        verbose_name_plural = 'Blocos'


class Morador(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    apto_sala = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    situacao = models.CharField(max_length=1, default='A', editable=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    estado = models.CharField(
        max_length=2,
        default='SC',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    situacao = models.CharField(max_length=1, default='A')

    def __str__(self) -> str:
        return self.nome or self.bloco.nome

    class Meta:
        verbose_name = 'Morador'
        verbose_name_plural = 'Moradores'
