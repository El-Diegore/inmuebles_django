from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class UserForm(UserCreationForm):
    first_name = forms.CharField()
    first_name.label = 'Nombre'
    last_name = forms.CharField()
    last_name.label = 'Apellido'
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email','password1', 'password2')
        labels = {'username': _('Nombre de Usuario')}
class TipoForm(forms.Form):
    tipos =((1, 'Arrendatario'),(2,'Arrendador'),)
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='rut', max_length=100)
    direccion = forms.CharField(label='direccion', max_length=100)
    telefono = forms.CharField(label='telefono',max_length=100) 
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name', 'email']
            