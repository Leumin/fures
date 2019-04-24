from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError



def ver_plato(req, id):
    plato = Plato.objects.filter(id=id).first()
    return JsonResponse({
        'id': plato.id,
        'nombre_plato': plato.nombre_plato,
        'precio': plato.descripcion,
        'estado': plato.estado,
        'menu': plato.menu
    })


def crear_plato(req):
    errores = []
    exito = True
    try:
        nuevo_plato = Plato()
        nuevo_plato.nombre_plato = req.POST.get('nombre_plato', None)
        nuevo_plato.precio = req.POST.get('precio', None)
        nuevo_plato.estado = req.POST.get('estado', None)
        nuevo_plato.menu = req.POST.get('menu', None)
        nuevo_plato.full_clean()
        nuevo_plato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_plato(req, id):
    errores = []
    exito = True
    try:
        plato = Plato.objects.filter(id=id).first()
        plato.nombre_plato = req.POST.get('nombre_plato', '')
        plato.precio = req.POST.get('precio', '')
        plato.estado = req.POST.get('estado', '')
        plato.menu = req.POST.get('menu', '')
        plato.full_clean()
        plato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })