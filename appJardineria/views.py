from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto,Categoria
from .forms import ProductoForm,CategoriaForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def gestion(request):
    context = {}
    return render(request, 'appJardineria/gestion.html', context)

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

def login(request):
    context={}
    return render(request, 'appJardineria/login.html', context)

def registro(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'appJardineria/registro.html', context)

def productos_list(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    print("Enviando datos de productos_list")
    return render(request, 'appJardineria/productos_list.html', context)


def productosAdd(request):
    print("Enviando datos de productos_add")
    context = {}

    if request.method == "POST":
        print("controlador es un post")
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            print("formulario es valido")
            form.save()
            
            # limpiar form
            form = ProductoForm()
            context = {'mensaje': "Ok, datos grabados...", "form": form}
        else:
            print("formulario no es valido")
            print(form.errors)
            context = {'form': form}
        return render(request, 'appJardineria/productosAdd.html', context)
    
    else:
        form = ProductoForm()
        context = {'form': form}
        return render(request, 'appJardineria/productosAdd.html', context)

    
def productos_del(request,pk):
    mensajes=[]
    errores=[]
    productos=Producto.objects.all()
    try:
        producto=Producto.objects.get(id_producto=pk)
        context={}
        if producto:
            producto.delete()
            mensajes.append("Producto eliminado")
            context= {'productos':productos, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'appJardineria/productos_list.html', context)
    except:
        print("Error al eliminar producto")
        productos=Producto.objects.all()
        mensaje="Error al eliminar producto"
        context={'mensaje':mensaje, 'productos':productos}
        return render(request, 'appJardineria/productos_list.html', context)
    


def productos_edit(request,pk):
    try:
        producto=Producto.objects.get(id_producto=pk)
        context={}
        if producto:
            print("Producto encontrado")
            if request.method == "POST":
                print("ESTO ES UN POST")
                form=ProductoForm(request.POST,request.FILES, instance=producto)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context= { 'producto':producto, 'form': form,'mensaje': mensaje}
                return render(request,'appJardineria/productos_edit.html', context)
            else:
                #no es un post
                print("No es un post")
                form=ProductoForm(instance=producto)
                mensaje=""
                context={'producto':producto, 'form':form,'mensaje':mensaje}
                return render(request, 'appJardineria/productos_edit.html', context)
    except:
        print("Error, id no existe")
        productos=Producto.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'productos':productos}
        return render(request, 'appJardineria/productos_list.html', context)


def categorias_list(request):
    categorias=Categoria.objects.all()
    context={'categorias':categorias}
    print("Enviando datos de categorias_list")
    return render(request, 'appJardineria/categorias_list.html', context)


def categoriasAdd(request):
    print("Enviando datos de categorias_add")
    context = {}

    if request.method == "POST":
        print("controlador es un post")
        form = CategoriaForm(request.POST)
        if form.is_valid():
            print("formulario es valido")
            form.save()
            
            # limpiar form
            form = CategoriaForm()
            context = {'mensaje': "Ok, datos grabados...", "form": form}
        else:
            print("formulario no es valido")
            print(form.errors)
            context = {'form': form}
        return render(request, 'appJardineria/categoriasAdd.html', context)
    
    else:
        form = CategoriaForm()
        context = {'form': form}
        return render(request, 'appJardineria/categoriasAdd.html', context)


# Validacion de sesiones #
def menu(request):
    request.session["usuario"]="cgarcia"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, )