from django.contrib import admin
from . import models


class LeituraAdmin(admin.ModelAdmin):
    def nome_bloco(self, obj):
        return obj.bloco.nome

    list_display = ['mesano', 'conta', 'morador', 'leitura_inical',
                    'leitura_final', 'data_leitura']


admin.site.register(models.Leituras, LeituraAdmin)
