from django import forms
from .models import Producto

from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','id_categoria','precio','imagen']
        labels = {
            'nombre': 'Nombre',
            'id_categoria': 'Categoría',
            'precio': 'Precio',
            'imagen': 'Imagen',
        }
        