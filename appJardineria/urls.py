from django.urls import path
from . import views


urlpatterns = [
    path('productos', views.productos, name='productos'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('home', views.home, name='home'),
    path('checkout', views.checkout, name='checkout'),

   path('productos_list', views.productos_list, name='productos_list'),
   path('productosAdd', views.productosAdd, name='productosAdd'),
   path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
   # path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),
]
