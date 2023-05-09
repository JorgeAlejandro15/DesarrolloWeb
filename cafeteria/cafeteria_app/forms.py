from django import forms
from .models import Proveedor
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
            