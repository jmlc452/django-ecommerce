from django.shortcuts import render,redirect
from .carro import Carro
from app_tienda.models import producto

from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def agregar_producto(request,producto_id,cantidad):
    carro = Carro(request)
    product=producto.objects.get(id=producto_id)
    carro.agregar(producto=product,cantidad=cantidad)
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

@login_required(login_url='login')
def eliminar_producto(request,producto_id):
    carro = Carro(request)
    product=producto.objects.get(id=producto_id)
    carro.eliminar(producto=product)
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

@login_required(login_url='login')
def restar_producto(request,producto_id):
    carro = Carro(request)
    product=producto.objects.get(id=producto_id)
    carro.restar_producto(producto=product)
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

@login_required(login_url='login')
def limpiar_carro(request,producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)
