from django.shortcuts import render , redirect
from .models import Proveedor,Producto       
from .forms import ProveedorForm 
#nuevo
from django.views.generic import ListView
from django.db import IntegrityError 
from django.contrib import messages 
from django.http.response import JsonResponse  
# Create your views here.

def Principal(request):
    return render(request,"Principal.html")

def stringL(lista):   #función para convertir a String una lista
    lista = lista
    s = ''
    for i in lista:
        s+= f'{i}, '
    s = s[0:-2] 
    return s


class ProveedorClass(ListView):
    Model = Proveedor
    template_name = 'proveedores.html' 
   

    # def registrarProveedor(request): 
    #     proveedores = Proveedor.objects.all()  
    #     data = {
    #         'form': ProveedorForm()
    #     }
    #     if request.method == 'POST':
    #         proveedores = ProveedorForm(data=request.POST)
    #         if proveedores.is_valid():
    #             proveedores.save()
    #             messages.success(request,"El proveedor se ha registrado")
    #             return redirect('/')
    #         else:
    #             data["form"] = proveedores  
    #     return render(request,'proveedores.html',data) 

    def RegProv(request):
        return render(request, "proveedores.html")



    def registrarProveedor(request):  
        try:
            ci = request.POST['ci']
            nombre = request.POST['nombre']
            telefono = request.POST['telefono'] 
            correo = request.POST['correo']
           
            proveedor = Proveedor.objects.create(ci=ci, nombre=nombre, telefono = telefono, correo = correo)
            # productos = request.POST.get('nombre_producto')
            # productos = stringL(productos)   
            
            nombre_producto = request.POST.getlist('nombre_producto')  
            precio = 0
            for i in range(len(nombre_producto)):
                nombres = nombre_producto[i]
                producto = Producto(nombre=nombres,precio=precio,proveedor=proveedor) 
                producto.save()   
            # proveedor.productos.add(*productos)
            
             
            messages.success(request,"El proveedor se ha registrado")
            return render(request,'proveedores.html')  
         
        except IntegrityError as i:  
            if 'UNIQUE constraint failed' in str(i):
            # manejo de excepción de campo único duplicado aquí
                messages.error(request,"Ya existe ese carnet") 
                return render(request, "proveedores.html")   


    def listarProveedor(request):
        proveedoresL = Proveedor.objects.all()  
        # productos = Producto.objects.filter(proveedor = proveedoresL)
        # productos = {} 
        # for proveedor in proveedoresL:
        #     productos[proveedor.ci] = Producto.objects.filter(proveedor=proveedor)
        data = {
            'object_list': proveedoresL 
        }  
        
        return render(request,"listarProveedores.html",data)             

    
                
    def edicionProveedor(request,ci): 
        proveedor = Proveedor.objects.get(ci=ci)
        return render(request, "edicionProveedor.html", {"proveedor": proveedor})


    def editarProveedor(request):
        ci = request.POST['ci']       # ci es el nombre que tiene el input en el html
        nombre = request.POST['nombre']
        telefono = request.POST['telefono'] 
        correo = request.POST['correo']
        
        proveedor = Proveedor.objects.get(ci=ci)
        proveedor.nombre = nombre
        proveedor.telefono = telefono
        proveedor.correo = correo 
        # proveedor.productos = productos       
        proveedor.save()
        messages.success(request,"El proveedor ha sido actualizado")
        return redirect('/listarProveedor/') 
  

    def eliminarProveedor(request, ci):
        proveedor = Proveedor.objects.get(ci=ci)  
        proveedor.delete() 
        messages.success(request,"El proveedor ha sido eliminado")
        return redirect('/listarProveedor/')  



class ProductoClass(ListView):
    Model = Producto
    template_name = 'listarProducto.html'

    def listarProducto(request,ci):
        proveedor = Proveedor.objects.get(ci=ci)
        productos = Producto.objects.filter(proveedor=proveedor)
        data = {
            'productos':productos
        }
        return render(request,"listarProducto.html",data)


    def edicionProducto(request,id):  
        productos = Producto.objects.get(id=id)     
        return render(request, "edicionProducto.html", {"productos": productos})


    def editarProducto(request):
        id = request.POST['id']  
        ci = request.POST['ci']
        nombre = request.POST['producto']
        # proveedor = request.POST['nombre'] 
        proveedor = Proveedor.objects.get(ci=ci)
        productos = Producto.objects.filter(proveedor=proveedor)
        data = {
            'productos':productos
        }
        producto = Producto.objects.get(id=id)  
        producto.nombre = nombre
        
        producto.save()
        messages.success(request,"El producto ha sido actualizado")
        return render(request ,"listarProducto.html" ,data) 


    def eliminarProducto(request, id):
        producto = Producto.objects.get(id=id) 
        ci = producto.proveedor.ci 
        proveedor = Proveedor.objects.get(ci=ci) 
        productos = Producto.objects.filter(proveedor=proveedor) 
        data = {
            'productos':productos 
        }
        producto.delete() 
        messages.success(request,"El producto ha sido eliminado")
        return render(request, "listarProducto.html" ,data)   
