from  django import forms
from .models import ContactForm

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