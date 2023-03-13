from django.contrib import admin
from . import models


class CalculoAdmin(admin.ModelAdmin):
    list_display = ['anomes', 'condominio', 'conta',
                    'valor', 'tipo_calculo']


admin.site.register(models.Calculos)
