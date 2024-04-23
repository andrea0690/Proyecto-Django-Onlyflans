from django.shortcuts import get_object_or_404, render, redirect
from .forms import ContactFormForm, UserForm
from .models import CarritoItem, Flan, Carrito
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
import json

# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private = False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def exito(request):
    return render(request, 'exito.html')

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormForm()

    return render(request, 'contacto.html', {'form': form})

def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)

    redirect_to = 'welcome' if request.user.is_authenticated else 'index'
    return render(request, 'flan_detail.html', {'flan':flan, 'redirect_to': redirect_to})

@login_required
def carrito(request, carrito_uuid):
    carrito = get_object_or_404(Carrito, carrito_uuid=carrito_uuid)
    carrito_items = CarritoItem.objects.filter(carrito=carrito)
    items = [{
        "id": item.id,
        "cantidad": item.cantidad,
        "flan": item.flan,
        "total": int(item.cantidad) * int(item.flan.precio),
    } for item in carrito_items]
    return render(request, 'carrito.html', {'items':items, 'carrito':carrito})

@login_required
def carrito_change_status(request, carrito_uuid):
    carrito = get_object_or_404(Carrito, carrito_uuid=carrito_uuid)
    carrito.is_active = False
    carrito.save()
    return JsonResponse({
                'success': True,
                'message': 'Orden creada exitosamente!.',
            })

@login_required
def agregar_carrito(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        user_id = data.get('user_id')
        flan_id = data.get('flan_id')
        cantidad = data.get('cantidad', 1)

        try:
            user = User.objects.get(pk=user_id)
            flan = Flan.objects.get(pk=flan_id)

            # Buscar un carrito existente para el usuario
            carrito, created = Carrito.objects.get_or_create(user=user, is_active=True)

            # Verificar si el item ya está en el carrito
            item, item_created = CarritoItem.objects.get_or_create(
                carrito=carrito,
                flan=flan,
            )

            if not item_created:
                # Si ya existe, aumentar la cantidad
                item.cantidad += cantidad
                item.save()

            return JsonResponse({
                'success': True,
                'message': 'Flan agregado al carrito.',
                'carrito_uuid': str(carrito.carrito_uuid)
            })
        except (User.DoesNotExist, Flan.DoesNotExist) as e:
            return JsonResponse({
                'success': False,
                'message': str(e),
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Método no permitido.',
        })
    
def usuarios(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Para poder guardar la contraseña de forma encriptada
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserForm()

    return render(request, 'registration/registrate.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = '/'

