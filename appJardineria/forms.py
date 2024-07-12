from django import forms
from .models import Producto,Categoria
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields="__all__"
        
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields="__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        