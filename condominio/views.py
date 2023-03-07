from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .models import Condominio


def index(request):
    condominios = Condominio.objects.all()
    return render(request, 'condominio/index.html', {
        'condominios': condominios
    })


def ver_condo(request, condominio_id):
    condominio = Condominio.objects.get(id=condominio_id)
    return render(request, 'condominio/ver_condo.html', {
        'condominio': condominio
    })


# class ListaCondominio(ListView):
#    model = models.Condominio
#    template_name = 'condominio/lista.html'


# class DetalheCondominio(View):
#    def get(self, *args, **kwargs):
#        return HttpResponse('Detallhe')
