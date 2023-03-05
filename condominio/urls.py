from django.urls import path
from . import views

app_name = 'condomino'

urlpatterns = [
    path('', views.ListaCondominio.as_view(), name="Lista"),
    # path('', views.DetalheCondominio.as_view(), name="Detalhe"),
]
