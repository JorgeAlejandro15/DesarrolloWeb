from django import forms
from .models import Proveedor
from django.forms import ValidationError




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
         