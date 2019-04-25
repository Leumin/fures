
from .models import Restaurante, Horario, Servicio, Plato
from .models import Sucursal
from .models import ImangenSucursal

from django.contrib import admin

class restaurante(admin.ModelAdmin):
    fields = ['nombre', 'descripcion', 'imagen', 'estado', 'usuario']
    list_display = ('nombre', 'estado')

class inlineplato(admin.StackedInline):
    model = Plato
    extra = 15


class inlineimagen(admin.StackedInline):
    model = ImangenSucursal
    extra = 3


class inlinehorario(admin.StackedInline):
    model = Horario
    extra = 7
    max_num = 7

class inlineservicios(admin.StackedInline):
    model = Servicio
    extra = 4

class sucursal(admin.ModelAdmin):
    fields = ['direccion', 'telefono', 'descripcion','capacidad', 'estado', 'restaurante']
    list_display = ('direccion', 'telefono', 'capacidad', 'estado')
    list_filter = ['restaurante']
    inlines = [inlineimagen, inlinehorario,inlineservicios, inlineplato]


admin.site.register(Restaurante, restaurante)
admin.site.register(Sucursal, sucursal)
