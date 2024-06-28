from django.shortcuts import render
from .models import Producto,Categoria
from .forms import ProductoForm

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


def productos_list(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    print("Enviando datos de productos_list")
    return render(request, 'appJardineria/productos_list.html', context)


def productosAdd(request):
    print("Enviando datos de productos_add")
    context={}

    if request.method=="POST":
        print("controlador es un post")
        form=ProductoForm(request.POST)
        if form.is_valid():
            print("formulario es valido")
            form.save()
            
            #limpiar form
            form=ProductoForm()
            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request, 'appJardineria/productosAdd.html', context)
    else:
        form= ProductoForm()
        context={'form':form}
        return render(request, 'appJardineria/productosAdd.html', context)