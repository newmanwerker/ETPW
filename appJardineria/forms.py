from django import forms
from .models import Producto,Categoria

from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields="__all__"
        
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields="__all__"
        