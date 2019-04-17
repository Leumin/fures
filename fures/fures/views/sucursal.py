from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


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


def ver_sucursal(req):
    sucursal = serializers.serialize("json",Sucursal.objects.filter(restaurante__id=3))
    res = HttpResponse(sucursal, content_type="application/json")
    return  res


def crear_sucursal(req):
    errores = []
    exito = True
    try:
        nueva_sucursal = Sucursal()
        nueva_sucursal.direccion = req.POST.get('direccion', None)
        nueva_sucursal.telefono = req.POST.get('telefono', None)
        nueva_sucursal.hora_inicio = req.POST.get('hora_inicio', None)
        nueva_sucursal.hora_cierre = req.POST.get('hora_cierre', None)
        nueva_sucursal.capacidad = req.POST.get('capacidad', None)
        nueva_sucursal.estado = req.POST.get('estado', None)
        nueva_sucursal.restaurante = req.POST.get('restaurante', None)
        nueva_sucursal.full_clean()
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