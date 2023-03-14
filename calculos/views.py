from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from django.http import Http404
from . import models
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


class GeraCalculos(ListView):
    model = models.Morador
    template_name = 'calculos/cal_lista.html'
