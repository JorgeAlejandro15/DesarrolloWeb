from django import forms
from .models import Proveedor, Producto 
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User




class ProveedorForm(forms.ModelForm):  
    class Meta:
        model = Proveedor 
        fields = '__all__'

    def clean_ci(self):
        ci = self.cleaned_data["ci"]
        existe = Proveedor.objects.filter(ci=ci).exists() 

        if existe:
            raise ValidationError('Error')
        return ci 


class CustomUserCreationForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        

class Perfil_Usuario_Form(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username','first_name', 'last_name', 'email'] 

        def __init__(self, *args, **kwargs):
            super.__init__(*args,**kwargs)
            self.fields['username'].label = 'Usuario'
            self.fields['first_name'].label = 'Nombre'
            self.fields['last_name'].label = 'Apellidos'
            self.fields['email'].label = 'Correo'  
        
        def save(self, commit=True):
            perfil = super().save(commit=False)
            perfil.user = self.user
            if commit:
                perfil.save()
            return perfil


class Producto_Form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'