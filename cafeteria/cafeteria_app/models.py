from django.db import models


class Proveedor(models.Model):
    ci = models.CharField(primary_key=True, max_length=11,unique=True)                  
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=8)  
    correo = models.EmailField(max_length=210) 
    # productos = models.CharField(max_length=200)   

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre) 
 
        
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10 , decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre  
