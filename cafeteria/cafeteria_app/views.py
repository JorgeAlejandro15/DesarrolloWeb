from django.shortcuts import render , redirect
from .models import Proveedor,Producto       
from .forms import CustomUserCreationForm, Perfil_Usuario_Form, Producto_Form
from django.contrib.auth import authenticate,login  
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string 
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User
#nuevo
from .carrito import Carrito
from django.db import IntegrityError 
from django.contrib import messages 
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
import qrcode 
  
# Create your views here.

def Principal(request): 
    productos = Producto.objects.all() 
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,8)
        productos = paginator.page(page) 
    except:
        messages.error(request,'La página no existe')
        return redirect('/') 
    return render(request,"Principal.html", {'entity': productos, 'paginator':paginator})  


 #Función para buscar los productos
def buscar(request):
    busqueda = request.GET.get('buscador') 
     
    # productos = Producto.objects.all()
    if busqueda:
        producto = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(categoria__icontains = busqueda) 
        ).distinct()

    page = request.GET.get('page',1)
    try:
        paginator = Paginator(producto,8)
        producto = paginator.page(page) 
    except:
        messages.error(request,'La página no existe')
        return redirect('/')
    return render(request, "prueba.html", {'entity':producto, 'paginator':paginator})  


def PregFrec(request):
    return render(request, "faq.html") 

def Nosotros(request):
    return render(request, "nosotros.html") 

#Registro del Usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST) 
        #formulario.fields["username"].help_text = None 
         
        if formulario.is_valid():
            formulario.save()               
            user = authenticate(username=formulario.cleaned_data['username'], password = formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado satisfactoriamente")
            return redirect(to="principal")
        
        data['form'] = formulario 
    return render(request, 'registration/registro.html' , data)  


 #Editar Perfil de Usuario
@login_required
def perfil_usuario(request):
    user = request.user 
    perfil = User.objects.get(username=user) 
    if request.method == 'POST':
        form = Perfil_Usuario_Form(request.POST, instance=perfil) 
        if form.is_valid():
            perfil.save()
            messages.success(request, "Su perfil se ha actualizado")
            return redirect('perfil')
    else:
        form = Perfil_Usuario_Form(instance=perfil)  
    return render(request, 'registration/profile.html', {'form':form})          


   #Envío del Correo  
def contacto(request): 
    if request.method == 'POST':
        asunto = request.POST['asunto']
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        descripcion = request.POST['descripcion']
        
        
        template = render_to_string('correo/email_template.html', {
            'asunto': asunto,
            'nombre': nombre,
            'correo': correo,
            'descripcion': descripcion,  
            'telefono': telefono
        })
        email = EmailMessage(asunto, template, settings.EMAIL_HOST_USER,['george111333555@gmail.com']) 
        email.fail_silently = False
        email.send() 
        messages.success(request,"El correo se ha enviado")
        return redirect('/contacto/') 
    return render(request, 'correo/contacto.html')


class ProveedorClass(ListView): 
    Model = Proveedor
    template_name = 'proveedor/proveedores.html' 
   
    @permission_required('cafeteria.add_RegProv')
    def RegProv(request):
        return render(request, "proveedor/proveedores.html")


    @permission_required('cafeteria.add_registrarProveedor')
    def registrarProveedor(request):  
        try:
            ci = request.POST['ci']
            nombre = request.POST['nombre']
            telefono = request.POST['telefono'] 
            correo = request.POST['correo']
            descripcion = request.POST['descripcion'] 
           
            proveedor = Proveedor.objects.create(ci=ci, nombre=nombre, telefono = telefono, correo = correo, descripcion = descripcion)
                 
            messages.success(request,"El proveedor se ha registrado")
            return render(request,'proveedor/proveedores.html')  
         
        except IntegrityError as i:  
            if 'UNIQUE constraint failed' in str(i):
            # manejo de excepción de campo único duplicado aquí
                messages.error(request,"Ya existe ese carnet") 
                return render(request, "proveedor/proveedores.html")   


    @permission_required('cafeteria.view_listarProveedor')
    def listarProveedor(request):
        proveedoresL = Proveedor.objects.all()  
        data = {
            'object_list': proveedoresL 
        }        
        return render(request,"proveedor/listarProveedores.html",data)             

    
    @permission_required('cafeteria.change_edicionProveedor')           
    def edicionProveedor(request,ci): 
        proveedor = Proveedor.objects.get(ci=ci)
        return render(request, "proveedor/edicionProveedor.html", {"proveedor": proveedor})


    @permission_required('cafeteria.change_editarProveedor')
    def editarProveedor(request):
        ci = request.POST['ci']       # ci es el nombre que tiene el input en el html
        nombre = request.POST['nombre']
        telefono = request.POST['telefono'] 
        correo = request.POST['correo']
        descripcion = request.POST['descripcion']
        
        proveedor = Proveedor.objects.get(ci=ci)
        proveedor.nombre = nombre
        proveedor.telefono = telefono
        proveedor.correo = correo 
        proveedor.descripcion = descripcion
             
        proveedor.save()
        messages.success(request,"El proveedor ha sido actualizado")
        return redirect('/listarProveedor/') 
  
  
    @permission_required('cafeteria.delete_eliminarProveedor')
    def eliminarProveedor(request, ci):
        proveedor = Proveedor.objects.get(ci=ci)  
        proveedor.delete() 
        messages.success(request,"El proveedor ha sido eliminado")
        return redirect('/listarProveedor/')  





    #Productos
class ListarProducto(PermissionRequiredMixin, ListView):
    Model = Producto
    template_name = 'producto/listarProducto.html'
    permission_required = ('cafeteria.view_ListarProducto') 
    queryset = Producto.objects.all()

class CrearProducto(PermissionRequiredMixin, CreateView):
    model = Producto
    template_name = 'producto/producto.html'
    form_class = Producto_Form 
    permission_required = ('cafeteria.add_CrearProducto')
    def producto(self, request, *args, **kwargs):
        messages.success(request,'El producto se ha guardado')    
    success_url = reverse_lazy('listar_producto')

@permission_required('cafeteria.delete_eliminarProducto')
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)  
    producto.delete() 
    messages.success(request,"El producto ha sido eliminado")
    return redirect('/listar_producto/')  

class UpdateProducto(PermissionRequiredMixin, UpdateView):
    model = Producto
    template_name = 'producto/edicionProducto.html'
    form_class = Producto_Form 
    permission_required = ('cafeteria.change_UpdateProducto')
    success_url = reverse_lazy('listar_producto')



# Carrito
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar(producto)
    alert = "Mensaje"
    messages.success(request,'El producto '+ producto.nombre +' se ha agregado al carrito') 
    return redirect('/')

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = id)
    carrito.eliminar(producto)
    messages.success(request,'El producto '+ producto.nombre +' ha sido eliminado del carrito') 
    return redirect('/') 

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.restar(producto)
    messages.success(request,'El producto '+ producto.nombre +' ha sido actualizado') 
    return redirect('/') 

def limpiar_carrito(request):
    carrito = Carrito(request) 
    carrito.limpiar()
    return redirect('/')


def comprar(request):
    # Crea el código QR
    qr = qrcode.QRCode(version=1, box_size=9, border=2)
    data = "Factura" # URL o datos que se mostrarán en el código QR
    qr.add_data(data) 
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Devuelve la imagen como respuesta HTTP
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG") 
    return response 

@login_required
def imagen(request):  
    image = 'cafeteria\static\img\qr.jpg'
    return render(request, 'Principal.html', {'image':image})   