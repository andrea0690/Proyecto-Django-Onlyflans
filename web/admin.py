from django.contrib import admin
from .models import Carrito, Flan, ContactForm, CarritoItem

# Register your models here.
#Hace que podamos ver los modelos en la pagina web, este es el registro del modelo que se hizo en models
admin.site.register(Flan) 

# registramos el modelo del contact form
admin.site.register(ContactForm)
admin.site.register(Carrito)
admin.site.register(CarritoItem)