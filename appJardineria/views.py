from django.shortcuts import render
from .models import Producto

# Create your views here.
def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'appJardineria/productos.html', context)

def home(request):
    context={}
    return render(request, 'appJardineria/home.html', context) 
def checkout(request):
    context={}
    return render(request, 'appJardineria/checkout.html', context)
def nosotros(request):
    context={}
    return render(request, 'appJardineria/nosotros.html', context)
def contacto(request):
    context={}
    return render(request, 'appJardineria/contacto.html', context)

def checkout(request):
    context={}
    return render(request, 'appJardineria/checkout.html', context)