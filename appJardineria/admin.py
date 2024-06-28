from django.contrib import admin
from .models import Categoria, Producto

admin.site.register(Producto)
admin.site.register(Categoria)