from django.urls import path
from .views import ProveedorClass, ProductoClass
from . import views   

urlpatterns = [
    path('',views.Principal, name="principal"),
    path('registro/', views.registro, name='registro'), 
    path('',ProveedorClass.as_view(), name='GestiónProveedores'),  
    path('listarProveedor/', ProveedorClass.listarProveedor),   
    path('listarProducto/<ci>', ProductoClass.listarProducto),     
    path('registrar/', ProveedorClass.RegProv),  
    path('registrarProveedor/', ProveedorClass.registrarProveedor),    
    path('edicionProducto/<id>', ProductoClass.edicionProducto),  
    path('edicionProveedor/<ci>', ProveedorClass.edicionProveedor), 
    path('editarProveedor/', ProveedorClass.editarProveedor),
    path('editarProducto/', ProductoClass.editarProducto),
    path('eliminarProveedor/<ci>', ProveedorClass.eliminarProveedor),
    path('eliminarProducto/<id>', ProductoClass.eliminarProducto)    
] 
    