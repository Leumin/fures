
from .models import Restaurante, Horario
from .models import Sucursal
from .models import ImangenSucursal

from django.contrib import admin

class restaurante(admin.ModelAdmin):
    fields = ['nombre', 'descripcion', 'imagen', 'estado', 'usuario_administrador']
    list_display = ('nombre', 'estado')


class inlineimagen(admin.StackedInline):
    model = ImangenSucursal
    extra = 3


class inlinehorario(admin.StackedInline):
    model = Horario
    extra = 7
    max_num = 7


class sucursal(admin.ModelAdmin):
    fields = ['direccion', 'telefono', 'capacidad', 'estado', 'restaurante']
    list_display = ('direccion', 'telefono', 'capacidad', 'estado')
    list_filter = ['restaurante']
    inlines = [inlineimagen, inlinehorario]


admin.site.register(Restaurante, restaurante)
admin.site.register(Sucursal, sucursal)
