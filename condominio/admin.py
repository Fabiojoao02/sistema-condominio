from django.contrib import admin
from . import models


class BlocoInLine(admin.TabularInline):
    model = models.Bloco
    extra = 1


class CondominioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'Cidade', 'Estado',
                    'Bairro', 'Fracao_ideal_tem']
    inlines = [
        BlocoInLine
    ]


class MoradorInLine(admin.TabularInline):
    model = models.Morador
    extra = 1


class BlocoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [
        MoradorInLine
    ]


class MoradorAdmin(admin.ModelAdmin):
    def nome_bloco(self, obj):
        return obj.bloco.nome

    list_display = ['nome', 'cpf', 'telefone',
                    'email', 'estado', 'nome_bloco']


admin.site.register(models.Condominio, CondominioAdmin)
admin.site.register(models.Bloco, BlocoAdmin)
admin.site.register(models.Morador, MoradorAdmin)
