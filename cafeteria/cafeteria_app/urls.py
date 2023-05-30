from django.urls import path
from .views import ProveedorClass, ListarProducto, CrearProducto, UpdateProducto
from . import views   

urlpatterns = [
    path('',views.Principal, name="principal"),
    path('preguntas-frecuentes/', views.PregFrec, name="faq"), 
    path('contacto/', views.contacto , name="contacto"), 
    path('registro/', views.registro, name='registro'), 
    path('perfil/', views.perfil_usuario, name='perfil'),    
      #Proveedor 
    path('',ProveedorClass.as_view(), name='GestiónProveedores'),  
    path('listarProveedor/', ProveedorClass.listarProveedor),      
    path('registrar/', ProveedorClass.RegProv),  
    path('registrarProveedor/', ProveedorClass.registrarProveedor),
    path('edicionProveedor/<ci>', ProveedorClass.edicionProveedor), 
    path('editarProveedor/', ProveedorClass.editarProveedor),
    path('eliminarProveedor/<ci>', ProveedorClass.eliminarProveedor),
    #Producto    
    path('listar_producto/', ListarProducto.as_view(), name='listar_producto'),
    path('crear_producto/', CrearProducto.as_view(), name='crear_producto'),
    path('delete_producto/<id>/', views.eliminarProducto, name='delete_producto'),
    path('update_producto/<int:pk>/', UpdateProducto.as_view(), name='update_producto'),
    #Carrito
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),  
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
    path('pagar/', views.comprar, name="comprar"),  
    path('producto/', views.buscar, name="buscar"),
    path('modal', views.imagen, name="modal")
    
] 
    