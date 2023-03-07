from django.urls import path
from . import views

# app_name = 'condomino'

urlpatterns = [
    path('', views.index, name='indexs'),
    path('busca/', views.busca, name='busca'),
    path('<int:condominio_id>', views.ver_condo, name='ver_condo'),

    # path('', views.DetalheCondominio.as_view(), name="Detalhe"),
]
