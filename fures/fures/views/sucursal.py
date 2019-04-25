from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render

from ..models import *
from django.core.exceptions import ValidationError


def sucursalhtml(request, id):
    return render(request, 'usuario/restaurante.html')


def ver_sucursales(request):
    if 'nombre' in request.GET:
        sucursal = serializers.serialize("json",
                                     Sucursal.objects.filter(
                                         nombre__icontains=request.GET['nombre']))
    else:
        sucursal = serializers.serialize("json", Sucursal.objects.all())
    res = HttpResponse(sucursal, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_sucursales_por_restaurante(req, id):
    sucursal = serializers.serialize("json",Sucursal.objects.filter(restaurante__id=id))
    res = HttpResponse(sucursal, content_type="application/json")
    return  res

def ver_sucursales_admin(req):
    # restaurante = Restaurante.objects.filter(usuario__id=req.session['usuario_id']).first()
    sucursal = Sucursal.objects.filter(restaurante__id=1)
    return JsonResponse({
        'id': sucursal.id,
        'direccion': sucursal.direccion,
        'telefono': sucursal.telefono,
        'capacidad': sucursal.capacidad,
        'descripcion': sucursal.descripcion,
        'restaurante': str(sucursal.restaurante)

    })



def ver_imagenes(req, id):
    imagen = serializers.serialize("json",ImangenSucursal.objects.filter(sucursal__id=id))
    res = HttpResponse(imagen, content_type="application/json")
    return  res


def ver_horario(req, id):
    horario = serializers.serialize("json",Horario.objects.filter(sucursal__id=id))
    res = HttpResponse(horario, content_type="application/json")
    return  res

def servicios(req, id):
    servicios = serializers.serialize("json",Servicio.objects.filter(sucursal__id=id))
    res = HttpResponse(servicios, content_type="application/json")
    return  res


def ver_platos_sucursal(req, id):
    platos = serializers.serialize("json", Plato.objects.filter(Sucursal__id=id))
    res = HttpResponse(platos, content_type="application/json")
    return  res


def ver_sucursal(req, id):
    sucursal = Sucursal.objects.filter(id=id).first()
    return JsonResponse({
        'id': sucursal.id,
        'direccion': sucursal.direccion,
        'telefono': sucursal.telefono,
        'capacidad': sucursal.capacidad,
        'descripcion': sucursal.descripcion,
        'restaurante': str(sucursal.restaurante)

    })


def crear_sucursal(req):
    errores = []
    exito = True
    restaurante = Restaurante.objects.filter(usuario__id=req.session['usuario_id']).first()
    try:
        nueva_sucursal = Sucursal()
        nueva_sucursal.direccion = req.POST.get('direccion', None)
        nueva_sucursal.telefono = req.POST.get('telefono', None)
        nueva_sucursal.descripcion = req.POST.get('descripcion', None)
        nueva_sucursal.capacidad = req.POST.get('capacidad', None)
        nueva_sucursal.estado = req.POST.get('estado', None)
        nueva_sucursal.restaurante_id = restaurante.id
        # nueva_sucursal.full_clean()
        nueva_sucursal.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_sucursal(req, id):
    errores = []
    exito = True
    try:
        sucursal = Sucursal.objects.filter(id=id).first()
        sucursal.direccion = req.POST.get('direccion', '')
        sucursal.telefono = req.POST.get('telefono', '')
        sucursal.hora_inicio = req.POST.get('hora_inicio', '')
        sucursal.hora_cierre = req.POST.get('hora_cierre', '')
        sucursal.capacidad = req.POST.get('capacidad', '')
        sucursal.estado = req.POST.get('estado', '')
        sucursal.restaurante = req.POST.get('restaurante', '')
        sucursal.full_clean()
        sucursal.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })