from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import Producto
from servicio.forms import ProductoForm


def servicio (request):    
    return render(request, "servicio/servicio.html")

    
class CrearServicio(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'servicio/servicio.html'
    success_url = reverse_lazy('servicio:servicio')

