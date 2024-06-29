from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria  = models.AutoField(db_column='idCategoria', primary_key=True) 
    nombre_categoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_categoria)

class Producto(models.Model):
    id_producto      = models.AutoField(db_column='idProducto', primary_key=True)
    nombre           = models.CharField(max_length=20)
    id_categoria     = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')   
    precio           = models.IntegerField()
    imagen           = models.ImageField(upload_to='productos/', null=False)
    descripcion      = models.TextField( blank=True, null=True)
    def __str__(self):
        return str(self.nombre)