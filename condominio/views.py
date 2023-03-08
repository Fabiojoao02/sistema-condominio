from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from .models import Condominio
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    condominios = Condominio.objects.order_by('-id').filter(
        mostrar=True
    )  # -nomeordem decrescente
    paginator = Paginator(condominios, 10)  # Show 10 contacts per page.

    page = request.GET.get('p')
    condominios = paginator.get_page(page)

    return render(request, 'condominio/index.html', {
        'condominios': condominios
    })


def ver_condo(request, condominio_id):
    condominio = Condominio.objects.get(id=condominio_id)
    # condominio = get_list_or_404(Condominio, id=condominio_id)
    if not Condominio.mostrar:
        raise Http404()

    return render(request, 'condominio/ver_condo.html', {
        'condominio': condominio
    })


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio'
        )
        # messages.add_message(
        #     request,
        #     messages.SUCCESS,
        #     'Menssagem de sucesso'
        # )
        return redirect('indexs')

    campos = Concat('nome', Value(' '), 'Endereco')

    condominios = Condominio.objects.annotate(
        nome_completo=campos
    ).filter(
        nome_completo__icontains=termo
    )

    # segunda forma de fazer a pesquisa
    # condominios = Condominio.objects.order_by('-id').filter(
    #    Q(nome__icontains=termo) | Q(Endereco__icontains=termo),
    #    mostrar=True
    # )  # -nomeordem decrescente

    paginator = Paginator(condominios, 10)  # Show 10 contacts per page.
    # print(condominios.query)
    page = request.GET.get('p')
    condominios = paginator.get_page(page)

    return render(request, 'condominio/busca.html', {
        'condominios': condominios
    })


# class ListaCondominio(ListView):
#    model = models.Condominio
#    template_name = 'condominio/lista.html'


# class DetalheCondominio(View):
#    def get(self, *args, **kwargs):
#        return HttpResponse('Detallhe')
