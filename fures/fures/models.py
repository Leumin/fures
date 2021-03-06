from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Categoria(models.Model):#Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45,error_messages={
        'max_length':'Este campo no puede exceder los 45 caracteres',
        'null':'Este campo no puede quedar null, por favor proporcione una descripcion',
        'blank':'Este campo no puede quedar vacío, por favor proporcione una descripcion'
    })

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=45)
    correo = models.EmailField(error_messages={
        'invalid':'Correo no valido'
    })
    telefono = models.CharField(max_length=8,error_messages={
        'max_length':'Ha excedido la cantidad permitida(8) de caracteres en el telefono',
        'null':'Este campo no puede quedar null, por favor proporcione un numero de telefono',
        'blank':' Este campo no puede quedar vacío, por favor proporcione un numero de telefono'
    })
    comentario = models.TextField(max_length=999, error_messages={
        'max_length': 'Al parecer ha sobrepasado la cantidad permitida(999 de caracteres)'
    })

class CategoriaRestaurante(models.Model):
    unique_together = ("Categoria","Restaurante")


class Comentario(models.Model):#Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.PROTECT)
    comentario = models.TextField(max_length=100,error_messages={
        'max_length': 'Al parecer ha sobrepasado la cantidad permitida(100 de caracteres)'
    })
    puntuacion = models.IntegerField()


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_plato = models.TextField(max_length=45,error_messages={
        'max_length':'Al parecer ha sobrepasado la cantidad permitida(45) de caracteres',
        'null':'El nombre del plato no puede quedar null, por favor proporcione el nombre del plato',
        'blank':'El nombre del plato no puede quedar vacío, por favor proporcione el nombre del plato'
    })
    precio = models.DecimalField(max_digits=6, decimal_places=2,error_messages={

        'null':'Por favor ingrese una cantidad para el precio',
        'blank':'Este campo no puede quedar vacio, por favor ingrese una cantidad para el precio'
    })
    imagen = models.ImageField(upload_to='platos', blank=False, null=False)
    estado = models.BooleanField(default=True)#verificar que tipo de validaciones se puede hacer aqui
    Sucursal = models.ForeignKey('Sucursal', on_delete=models.PROTECT)#verificar que tipo de validaciones se puede hacer aqui


class Promocion(models.Model):#Se agregaron validaciones
    id = models.AutoField(primary_key=True,max_length=11)#verificar esta parte con la BD
    descripcion = models.TextField(max_length=5000,error_messages={
        'max_length':'Al parecer ha sobrepasado la cantidad permitida(5000) de caracteres'
    })
    fecha_inicio = models.DateField(error_messages={
        'null':'Este campo no puede quedar null, por favor proporcione los datos que se piden',
        'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden'
    })
    fecha_final = models.DateField(error_messages={
        'null':'Este campo no puede quedar null, por favor proporcione los datos que se piden',
        'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden'
    })
    sucursal = models.ForeignKey('Sucursal',on_delete=models.PROTECT)

class Reserva(models.Model):#Se agregaron validaciones
    id = models.AutoField(primary_key=True, max_length=11)
    hora_fecha_reserva = models.DateTimeField(error_messages={
        'null':'Este campo no puede quedar null, por favor proporcione los datos que se piden',
        'blank':'Este campo no puede quedar vacío, por favor proporcione los datos que se piden'
    })
    estado_reserva = models.BooleanField()#verificar esta parte con la BD
    cantidad_personas = models.IntegerField(error_messages={
        'null':'Este campo no puede quedar null, por favor proporcione los datos que se piden',
        'blank':'Este campo no puede quedar vacío, por favor proporcione los datos que se piden'
    })

    sucursal = models.ForeignKey('Sucursal',on_delete=models.PROTECT)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    motivo_cancelacion = models.TextField(max_length=1000,blank=True,null=True,error_messages={
        'max_length':'Al parecer a sobrepasado la cantidad permitida(1000) de caracteres'
    })#verificar esta parte con la BD


class Restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300,error_messages={
        'max_length':'Este campo no puede contener mas de 300 caracteres',
        'null':'Este campo no puede quedar null, por favor proporcione un nombre para el restaurante',
        'blank':'Este campo no puede quedar vacío, por favr proporcione un nombre para el restaurante'
    })#verificar esta parte con la BD
    descripcion = models.TextField(max_length=1000,error_messages={
        'max_length':'Este campo no puede contener mas de 1000 caracteres'
    })#verificar esta parte con la BD
    imagen = models.ImageField(upload_to='restaurantes', blank=False, null=False)
    estado = models.BooleanField()#verificar esta parte con la BD
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre

class Rol(models.Model):#Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=45,error_messages={
        'max_length':'Este campo no puede contener mas de 45 caracteres',
        'null':'Este campo no puede quedar null, por favor proporcione una descripcion para este rol',
        'blank':'Este campo no puede quedar blank, por favor proporcione una descripcion para este rol'
    })

class Servicio(models.Model):#Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=45,error_messages={
        'max_length':'Este campo no puede contener mas de 45 caracteres',

    })
    imagen = models.ImageField(upload_to='iconos', blank=False, null=False)
    sucursal = models.ForeignKey('Sucursal',on_delete=models.PROTECT)


class Sucursal(models.Model): #Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=700,error_messages={
        'max_length': 'Ha excedido la cantidad permitida(700) de caracteres en la direccion de la sucursal',
        'null': ' Este campo no puede quedar null, por favor proporcione una direccion para la sucursal',
        'blank':' Este campo no puede quedar vacío, por favor proporcione una direccion para la sucursal'
    })
    telefono = models.CharField(max_length=8,error_messages={
        'max_length':'Ha excedido la cantidad permitida(8) de caracteres en el telefono',
        'null':'Este campo no puede quedar null, por favor proporcione un numero de telefono',
        'blank':' Este campo no puede quedar vacío, por favor proporcione un numero de telefono'
    })

    descripcion = models.TextField(max_length=999, error_messages={
        'max_length': 'Este campo no puede contener mas de 45 caracteres',

    })
    capacidad = models.IntegerField(error_messages={
        'null':'Es necesario ingresar una cantidad para la capacidad',
        'blank':'Este campo no puede quedar vacío, por favor ingrese una cantidad para la capacidad'
    })
    estado = models.BooleanField(default=True)
    restaurante = models.ForeignKey('Restaurante',on_delete=models.PROTECT)

    def __int__(self):
        return self.restaurante



class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=15, error_messages={
        'max_length': 'Ha excedido la cantidad permitida(15) de caracteres',
        'null': ' Este campo no puede quedar null',
        'blank': ' Este campo no puede quedar vacío'
    })
    hora_inicio = models.TimeField(error_messages={
        'null': 'Este campo no puede quedar null, por favor proporcione una hora de inicio',
        'blank': 'Este campo no puede quedar vacío, por favor proporcione una hora de inicio'
    })
    hora_cierre = models.TimeField(error_messages={
        'null': 'Este campo no puede quedar null, por favor proporcione una hora de cierre',
        'blank': 'Este campo no puede quedar vacío, por favor proporcione una hora de cierre'
    })
    sucursal = models.ForeignKey('Sucursal', on_delete=models.PROTECT)


class ImangenSucursal(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='sucursales', blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.PROTECT)
# class TipoUsuario(models.Model): # Se agregaron validaciones
#     id = models.AutoField(primary_key=True)
#     descripcion = models.CharField(max_length=45,error_messages={
#         'max_length':'La descripcion  de tipo de usuario no puede exceder los 45 caracteres permitidos',
#         'null':'Este campo no puede quedar null, por favor complete la descripcion',
#         'blank':'Este campo no puede quedar vacío, por favor complete la descripcion'
#     })

class Usuario(models.Model):    # Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    nombre_persona = models.CharField(max_length=45, error_messages={
                                          'max_length': 'El Nombre no puede ser mayor a 45  caracteres ',
                                          'null': 'Este campo no puede quedar null, por favor proporcione un Nombre de Usuario',
                                          'blank': 'Este campo no puede quedar vacío, por favor proporcione un Nombre de Usuario'
                                      })
    def clean(self):
        if not self.nombre_persona.isalpha():
            raise ValidationError("El nombre de la persona solamente puede contener datos alfabeticos")

    apellido_persona = models.CharField(max_length=45,error_messages={
                                          'max_length': 'EL Apellido no puede ser mayor a 45  caracteres ',
                                          'null': 'Este campo no puede quedar null, por favor proporcione un Apellido ',
                                          'blank': 'Este campo no puede quedar vacío, por favor proporcione un Apellido '
                                      })

    def clean(self):
        if not self.apellido_persona.isalpha():
            raise ValidationError("El apellido de la persona solamente puede contener datos alfabeticos")

    direccion = models.TextField(max_length=700,error_messages={
                                          'max_length': 'La direccion de Usuario no puede ser mayor a 700  caracteres ',
                                          'null': 'Este campo no puede quedar null, por favor proporcione una direccion de Usuario',
                                          'blank': 'Este campo no puede quedar vacío, por favor proporcione una direccion de Usuario'
                                      })
    nombre_usuario = models.CharField(unique=True, max_length=45,error_messages={
                                          'max_length': 'El nombre de Usuario no puede ser mayor a 45  caracteres ',
                                          'null': 'Este campo no puede quedar null, por favor proporcione Nombre de Usuario',
                                          'blank': 'Este campo no puede quedar vacío, por favor proporcione un Nombre de Usuario'
                                      })
    contrasena = models.CharField(max_length=45,error_messages={
                                          'max_length': 'La contraseña de Usuario no puede ser mayor a 45  caracteres ',
                                          'null': 'Este campo no puede quedar null, por favor proporcione una contraseña de Usuario',
                                          'blank': 'Este campo no puede quedar vacío, por favor proporcione una contraseña de Usuario'
                                      })
    correo = models.EmailField(error_messages={
        'invalid':'Correo no valido'
    })
    telefono = models.CharField(max_length=8,error_messages={
        'max_length':'El telefono no puede contener mas de 8 caracteres',
        'null': 'Este campo no puede quedar null, por favor proporcione un telefono',
        'blank': 'Este campo no puede quedar vacío, por favor proporcione un telefono'
    })

    estado = models.BooleanField(default=True)
    tipo_usuario = models.ForeignKey('TipoUsuario',on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre_persona


class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)


class CategoriaPlato(models.Model):# Se agregaron validaciones
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100,error_messages={
        'max_length':'La descripcion  de la categoria del plato no puede contener mas de 100 caracteres',
        'null':'Este campo no puede quedar null, por favor proporcione una categoria para el plato',
        'blank':'Este campo no puede quedar vacío, por favor proporcione una categoria para el plato'
    })


class CategoriaPlatoPlato(models.Model):
    unique_together = ("CategoriaPlato","Plato")


