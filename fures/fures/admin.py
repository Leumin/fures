
from .models import Restaurante
from .models import Sucursal
from .models import ImangenSucursal

from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Usuario

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class UsuarioInline(admin.StackedInline):
#     model = Usuario
#     can_delete = False
#     verbose_name_plural = 'usuario'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (UsuarioInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)



class restaurante(admin.ModelAdmin):
    fields = ['nombre', 'estado', 'descripcion']
    list_display = ('nombre', 'estado')


class sucursal(admin.ModelAdmin):
    fields = ['direccion', 'telefono', 'hora_inicio', 'hora_cierre', 'capacidad', 'estado', 'restaurante']
    list_display = ('direccion', 'telefono', 'capacidad', 'estado')
    list_filter = ['restaurante']


admin.site.register(Restaurante, restaurante)
admin.site.register(Sucursal, sucursal)
admin.site.register(ImangenSucursal)