from django.db import models
from django.conf import settings

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

class CategoriaRestaurante(models.Model):
    #id_categoria_restaurante = models.ForeignKey('Categoria',on_delete=models.PROTECT,primary_key=True)
    #id_restaurante = models.ForeignKey('Restaurantes', on_delete=models.PROTECT,primary_key=True)
    unique_together = ("Categoria","Restaurante")

class Comentario(models.Model):
    #id_sucursal = models.ForeignKey('Sucursales',on_delete=models.PROTECT)
    #id_usuario = models.ForeignKey('Usuario',on_delete=models.PROTECT)
    unique_together = ("Sucursal","Usuario")
    comentario = models.TextField(max_length=100)
    puntuacion = models.IntegerField()


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre_menu = models.TextField(max_length=30)
    descripcion = models.TextField(max_length=50,blank=True)

class MenuSucursal(models.Model):
    #id_menu = models.ForeignKey('Menu',on_delete=models.PROTECT,primary_key=True)#verificar esta parte con la BD
    #id_sucursal = models.ForeignKey('Sucursales',on_delete=models.PROTECT,primary_key=True)
    unique_together = ("Menu","Sucursal")

class Plato(models.Model):
    id_plato = models.AutoField(primary_key=True)
    nombre_plato = models.TextField(max_length=45)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    estado = models.BooleanField(default=True)#verificar esta parte con la BD
    menu = models.ForeignKey('Menu', on_delete=models.PROTECT)


class Promocion(models.Model):
    id_promocion = models.AutoField(primary_key=True,max_length=11)#verificar esta parte con la BD
    descripcion = models.TextField(max_length=5000)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_final = models.DateField()
    id_sucursal = models.ForeignKey('Sucursal',on_delete=models.PROTECT)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True, max_length=11)
    hora_fecha_reserva = models.DateTimeField()
    estado_reserva = models.BooleanField()#verificar esta parte con la BD
    cantidad_personas = models.IntegerField()
    sucursal = models.ForeignKey('Sucursal',on_delete=models.PROTECT)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    motivo_cancelacion = models.TextField(max_length=1000,blank=True)#verificar esta parte con la BD


class Restaurante(models.Model):
    id_restaurante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)#verificar esta parte con la BD
    descripcion = models.TextField(max_length=1000)#verificar esta parte con la BD
    estado = models.BooleanField()#verificar esta parte con la BD

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=45)

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=45)
    id_sucursal = models.ForeignKey('Sucursal',on_delete=models.PROTECT)


class Sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=700)#verificar esta parte con la BD
    telefono = models.CharField(max_length=8)
    hora_inicio = models.TimeField()
    hora_cierre = models.TimeField()
    capacidad = models.IntegerField()
    estado = models.BooleanField(default=True)
    restaurante = models.ForeignKey('Restaurante',on_delete=models.PROTECT)


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_persona = models.CharField(max_length=45)
    apellido_persona = models.CharField(max_length=45)
    direccion = models.TextField(max_length=700)
    nombre_usuario = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    correo = models.EmailField()
    telefono = models.CharField(max_length=8)
    estado = models.BooleanField(default=True)
    codigo_rol = models.ForeignKey('Rol',on_delete=models.PROTECT)

class UsuarioTipoUsuario(models.Model):
    #id_usuario = models.ForeignKey('Usuario',on_delete=models.PROTECT,primary_key=True)
    #id_tipo_usuario = models.ForeignKey('Tipo_Usuario',on_delete=models.PROTECT,primary_key=True)
    unique_together = ("Usuario","TipoUsuario")


class CategoriaPlato(models.Model):
    id_categoria_plato=models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)


class CategoriaPlatoPlato(models.Model):
    unique_together = ("CategoriaPlato","Plato")