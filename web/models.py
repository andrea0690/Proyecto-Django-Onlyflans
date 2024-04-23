from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Flan(models.Model): #tabla dentro la base de datos
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image_url = models.URLField(unique = True)
    slug = models.SlugField(unique = True , blank=True)
    is_private = models.BooleanField(default = False)
    precio = models.IntegerField(default=6000)

    def save(self, *args, **kwargs):
        # if self.id:
        #     super().save(self,*args,**kwargs)
        # else:
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(self,*args,**kwargs)

    def __str__(self):
        return self.name
    
# actividad 3
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.customer_name 
    
class Carrito(models.Model):
    carrito_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carritos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return f"Carrito de {self.user.username} creado el {self.fecha_creacion}"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE)  # Relación con Flan
    cantidad = models.PositiveIntegerField(default=1)  # Cantidad de cada producto en el carrito

    def __str__(self):
        return f"{self.cantidad} x {self.flan.name} en {self.carrito.carrito_uuid}"


# {
#     "carrito_uuid": "1234567890",
#     "user": 1,
#     "fecha_creacion": "2022-01-01",
#     "is_active": True,
#     "carritoIItems": [
#         {
#             "carrito": "1234567890",
#             "flan": 15,
#             "cantidad": 1
#         },
#         {
#             "carrito": "1234567890",
#             "flan": 14,
#             "cantidad": 10
#         },
#         {
#             "carrito": "1234567890",
#             "flan": 10,
#             "cantidad": 3
#         }
#     ]
# }