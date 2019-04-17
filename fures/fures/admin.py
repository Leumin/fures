
from .models import Restaurante
from .models import Sucursal
from .models import ImangenSucursal

from django.contrib import admin

class restaurante(admin.ModelAdmin):
    fields = ['nombre', 'estado', 'imagen', 'descripcion']
    list_display = ('nombre', 'estado')


class sucursal(admin.ModelAdmin):
    fields = ['direccion', 'telefono', 'hora_inicio', 'hora_cierre', 'capacidad', 'estado', 'restaurante']
    list_display = ('direccion', 'telefono', 'capacidad', 'estado')
    list_filter = ['restaurante']


admin.site.register(Restaurante, restaurante)
admin.site.register(Sucursal, sucursal)
admin.site.register(ImangenSucursal)