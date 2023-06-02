from django.db import models


class Proveedor(models.Model):
    ci = models.CharField(primary_key=True, max_length=11,unique=True)                  
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=8)  
    correo = models.EmailField(max_length=210) 
    descripcion = models.TextField(max_length=300)    

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre) 
 
        
class Producto(models.Model):
    nombre = models.CharField(verbose_name='Nombre del producto',max_length=100)
    precio = models.FloatField(verbose_name='Precio')  
    cantidad_productos = models.PositiveIntegerField(verbose_name='Cantidad de productos') 
    categoria = models.CharField(verbose_name='Categoría', max_length=10, choices=( 
        ('bebida', 'Bebida'),
        ('sandwich', 'Sandwich'),
        ('pasta', 'Pasta'),
        ('carne', 'Carne'),
        ('dulce', 'Dulce'),
        ('golosina', 'Golosina'),
        ('aseo', 'Aseo')
    ), default='bebida')
    imagen = models.ImageField(upload_to="productos", null=True) 
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos',verbose_name='Proveedor')

    def __str__(self):
        return self.nombre  


class Factura(models.Model):
    numero_de_factura = models.PositiveSmallIntegerField(verbose_name="Número", primary_key=True) 
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.FloatField(verbose_name="Precio")
    fecha = models.DateField(verbose_name="Fecha") 
    
    def __str__(self):
        return self.descripcion
    