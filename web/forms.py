from  django import forms
from .models import ContactForm 
from django.contrib.auth.models import User


# es el formulario que vamos a mostrar en la pagina web
class ContactFormForm(forms.ModelForm):
    # 
    # customer_email = forms.EmailField(label ='correo')
    # customer_name = forms.CharField(max_length=64, label = 'nombre')
    # message = forms.CharField(label='mensaje')
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        labels = {
            'customer_email': 'Correo electrónico',
            'customer_name': 'Nombre del cliente',
            'message': 'Deje su mensaje'
        }

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required', label="Email")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label="Pass")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Alias',
        }