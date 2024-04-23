"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('exito/', views.exito, name ='exito'),
    path('welcome/', views.welcome, name ='welcome'),
    path('contacto/', views.contacto, name ='contacto'),
    path('registrate/', views.usuarios, name='registrate'),
    path('registration/', include('django.contrib.auth.urls')), #busca las rutas del logueo de django
    path('flan/<int:flan_id>', views.flan_detail, name='detalle'),
    path('carrito/<str:carrito_uuid>', views.carrito, name='carrito'),
    path('agregar_carrito/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito_change_status/<str:carrito_uuid>', views.carrito_change_status, name='carrito_change_status')
]
