from django.urls import path
from . import views


urlpatterns = [
    path('favoritos/agregar/<int:pk>/', views.agregar_favorito, name='agregar_favorito'),
    path('favoritos/eliminar/<int:pk>/', views.eliminar_favorito, name='eliminar_favorito'),
    path('favoritos/', views.ver_favoritos, name='ver_favoritos'),
    path('productos/', views.productos, name='productos'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('home', views.home, name='home'),
    path('checkout', views.checkout, name='checkout'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('registro', views.registro, name='registro'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    #CRUD DE PRODUCTOS
   path('productos_list', views.productos_list, name='productos_list'),
   path('productosAdd', views.productosAdd, name='productosAdd'),
   path('gestion', views.gestion, name='gestion'),
   path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
   path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),
  #CRUD DE CATEGORIAS
   path('categorias_list', views.categorias_list, name='categorias_list'),
   path('categoriasAdd', views.categoriasAdd, name='categoriasAdd'),
]

    #CRUD DE CATEGORIAS
    