"""fures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.contacto import crear_msj_contacto
from .views.categoria import ver_categorias, ver_categoria, crear_categoria, actualizar_categoria
from .views.categoriaPlato import ver_categoriasPlato, ver_categoriaPlato, crear_categoriaPlato, \
    actualizar_categoriaPlato
from .views.comentario import ver_comentarios, ver_comentario, crear_comentario, actualizar_comentario
from .views.index import inicio, login, formularioRegistro
from .views.index_admin import sucursal, Visualizar_sucursal, Crear_Plato, Visualizar_Plato, Crear_Servicios, \
    crear_sucursales_html
from .views.menu import ver_menus, ver_menu, crear_menu, actualizar_menu
from .views.plato import ver_plato, crear_plato, actualizar_plato
from .views.promocion import ver_promociones, ver_promocion, crear_promocion, actualizar_promocion
from .views.resereva import ver_reservas, ver_reserva, crear_reserva, actualizar_reserva
from .views.restaurante import restauranteshtml, ver_restaurantes, ver_restaurante, crear_restaurante, \
    actualizar_restaurante, ultimos_restaurantes
from .views.rol import ver_roles, ver_rol, crear_rol, actualizar_rol
from .views.servicio import ver_servicios, ver_servicio, crear_servicio, actualizar_servicio
from .views.sucursal import ver_sucursales, ver_sucursales_por_restaurante, crear_sucursal, actualizar_sucursal, \
    sucursalhtml, ver_sucursal, ver_imagenes, ver_horario, ver_platos_sucursal, servicios, ver_sucursales_admin
from .views.tipoUsuario import ver_tiposUsuario, ver_tipoUsuario, crear_tipoUsuario, actualizar_tipoUsuario
from .views.usuario import ver_usuarios, ver_usuario, crear_usuario, actualizar_usuario, logueo, logout
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', inicio, name='inicio'),
    path('', login, name='login'),
    path('index/', formularioRegistro, name='formularioRegistro'),
    path('index_admin/', sucursal, name='sucursal'),
    path('index_admin/Visualizar/', Visualizar_sucursal, name='Visualizar_sucursal'),
    path('index_admin/Crear/', Crear_Plato, name='Crear_Plato'),
    path('index_admin/Visualizar/', Visualizar_Plato, name='Visualizar_Plato'),
    path('index_admin/crear/sucursal', crear_sucursales_html, name='crear_sucursal_html'),
    path('index_admin/Crear/servicio/', Crear_Servicios, name='Crear_Servicios'),

                  #CATEGORIAS
    path('categorias/', ver_categorias),
    path('categorias/ver/<int:id>/', ver_categoria, views.categoria),
    path('categorias/crear', crear_categoria),
    path('categorias/actualizar/<int:id>', actualizar_categoria),
    #RESTAURANTE
    path('restaurante/',restauranteshtml,name='restauranteshtml'),
    path('restaurante/ultimos', ultimos_restaurantes),
    path('restaurante/todos', ver_restaurantes),
    path('restaurante/ver/<int:id>/', ver_restaurante),
    path('restaurante/crear', crear_restaurante, name='crear_restaurante'),
    path('restaurante/actualizar/<int:id>', actualizar_restaurante),
    #MENU
    path('menu/', ver_menus),
    path('menu/ver/<int:id>/', ver_menu),
    path('menu/crear', crear_menu),
    path('menu/actualizar/<int:id>', actualizar_menu),
    #TIPOUSUARIO
    path('tipoUsuario/', ver_tiposUsuario),
    path('tipoUsuario/ver/<int:id>/', ver_tipoUsuario),
    path('tipoUsuario/crear', crear_tipoUsuario),
    path('tipoUsuario/actualizar/<int:id>', actualizar_tipoUsuario),
    #CATEGORIAPLATO
    path('categoriaPlato/', ver_categoriasPlato),
    path('categoriaPlato/ver/<int:id>/', ver_categoriaPlato),
    path('categoriaPlato/crear', crear_categoriaPlato),
    path('categoriPlato/actualizar/<int:id>', actualizar_categoriaPlato),
    #ROL
    path('rol/', ver_roles),
    path('rol/ver/<int:id>/', ver_rol),
    path('rol/crear', crear_rol),
    path('rol/actualizar/<int:id>', actualizar_rol),
    #SERVICIO
    path('servicio/', ver_servicios),
    path('servico/ver/<int:id>/', ver_servicio),
    path('servicio/crear', crear_servicio),
    path('servicio/actualizar/<int:id>', actualizar_servicio),
    #PLATO
    path('plato/ver/<int:id>/', ver_plato),
    path('plato/crear', crear_plato),
    path('plato/actualizar/<int:id>', actualizar_plato),
    #USUARIO
    path('usuario/', ver_usuarios),
    path('usuario/ver/<int:id>/', ver_usuario),
    path('usuario/login/', logueo, name ='logueo'),
    path('usuario/logout/', logout, name = 'logout'),
    path('usuario/crear', crear_usuario, name='crearusuario'),
    path('usuario/actualizar/<int:id>', actualizar_usuario),

    #RESERVA
    path('reserva/', ver_reservas),
    path('reserva/ver/<int:id>/', ver_reserva),
    path('reserva/crear', crear_reserva, name='createreserva'),
    path('reserva/actualizar/<int:id>', actualizar_reserva),
    #SUCURSAL
    path('sucursal/unico/<int:id>', sucursalhtml, name='sucursalhtml'),
    path('sucursal/', ver_sucursales),
    path('sucursal/imagen/<int:id>', ver_imagenes),
    path('sucursal/horario/<int:id>', ver_horario),
    path('sucursal/servicio/<int:id>', servicios),
    path('sucursal/platos/<int:id>', ver_platos_sucursal, name='verplatos'),
    path('sucursal/ver/<int:id>/', ver_sucursales_por_restaurante),
    path('sucursal/ver/admin/', ver_sucursales_admin),
    path('sucursal/ver/sucursal/<int:id>/', ver_sucursal),
    path('sucursal/crear', crear_sucursal, name="crearsucursal"),
    path('sucursal/actualizar/<int:id>', actualizar_sucursal),
    #PROMOCION
    path('promocion/', ver_promociones),
    path('promocion/ver/<int:id>/', ver_promocion),
    path('promocion/crear', crear_promocion),
    path('promocion/actualizar/<int:id>', actualizar_promocion),
    #COMENTARIO
    path('comentario/', ver_comentarios),
    path('comentario/ver/<int:id>/', ver_comentario),
    path('comentario/crear', crear_comentario, name='crearcomentario'),
    path('comentario/actualizar/<int:id>', actualizar_comentario),
    #contacto
    path('contacto/crear', crear_msj_contacto, name='crearcontacto'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
