from django.contrib import admin
from .models import Proveedor,Producto, Factura 

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto) 
admin.site.register(Factura) 