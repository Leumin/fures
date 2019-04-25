from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_servicios(request):
    if 'descripcion' in request.GET:
        servicio = serializers.serialize("json",
                                     Servicio.objects.filter(
                                         nombre__icontains=request.GET['descripcion']))
    else:
        servicio = serializers.serialize("json", Servicio.objects.all())
    res = HttpResponse(servicio, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_servicio(req, id):
    servicio = Servicio.objects.filter(id=id).first()
    return JsonResponse({
        'id': servicio.id,
        'descripcion': servicio.descripcion,
        'sucursal': servicio.sucursal
    })


def crear_servicio(req):
    errores = []
    exito = True
    try:
        nuevo_servicio = Servicio
        nuevo_servicio.descripcion = req.POST.get('descripcion', None)
        nuevo_servicio.imagen = req.FILES['imagen']
        nuevo_servicio.sucursal = req.POST.get('sucursal', None)
        nuevo_servicio.full_clean()
        nuevo_servicio.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_servicio(req, id):
    errores = []
    exito = True
    try:
        servicio = Sucursal.objects.filter(id=id).first()
        servicio.descripcion = req.POST.get('descripcion', '')
        servicio.sucursal = req.POST.get('sucursal', '')
        servicio.full_clean()
        servicio.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })