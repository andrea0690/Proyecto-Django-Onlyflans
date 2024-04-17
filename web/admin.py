from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.
#Hace que podamos ver los modelos en la pagina web, este es el registro del modelo que se hizo en models
admin.site.register(Flan) 

# registramos el modelo del contact form

admin.site.register(ContactForm)