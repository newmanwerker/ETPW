from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto,Categoria
from .forms import ProductoForm,CategoriaForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Favorito
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def gestion(request):
    context = {}
    return render(request, 'appJardineria/gestion.html', context)

@login_required(login_url='loginPage')
def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'appJardineria/productos.html', context)

def home(request):
    context={}
    return render(request, 'appJardineria/home.html', context) 

@login_required(login_url='loginPage')
def checkout(request):
    context={}
    return render(request, 'appJardineria/checkout.html', context)

def nosotros(request):
    context={}
    return render(request, 'appJardineria/nosotros.html', context)

def contacto(request):
    context={}
    return render(request, 'appJardineria/contacto.html', context)

@login_required(login_url='loginPage')
def checkout(request):
    context={}
    return render(request, 'appJardineria/checkout.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario o contraseña incorrectos')
        context={}
        return render(request, 'appJardineria/loginPage.html', context)

def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada correctamente para ' + user)
                return redirect('loginPage')
        context={'form':form}
        return render(request, 'appJardineria/registro.html', context)



def logoutUser(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def productos_list(request):
    productos=Producto.objects.all()
    context={'productos':productos}
    print("Enviando datos de productos_list")
    return render(request, 'appJardineria/productos_list.html', context)


@login_required(login_url='loginPage')
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
    

@login_required(login_url='loginPage')
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

@login_required(login_url='loginPage')
def categorias_list(request):
    categorias=Categoria.objects.all()
    context={'categorias':categorias}
    print("Enviando datos de categorias_list")
    return render(request, 'appJardineria/categorias_list.html', context)

@login_required(login_url='loginPage')
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




@login_required(login_url='loginPage')
def agregar_favorito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, producto=producto)
    if created:
        messages.success(request, f'{producto.nombre} añadido a tus favoritos')
    else:
        messages.info(request, f'{producto.nombre} ya está en tu lista de favoritos')
    return redirect('productos')

@login_required(login_url='loginPage')
def eliminar_favorito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    favorito = Favorito.objects.filter(usuario=request.user, producto=producto).first()
    if favorito:
        favorito.delete()
        messages.success(request, f'{producto.nombre} eliminado de tus favoritos')
    return redirect('ver_favoritos')

@login_required(login_url='loginPage')
def ver_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    context = {'favoritos': favoritos}
    return render(request, 'appJardineria/favoritos.html', context)