from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_promociones(request):
    if 'id' in request.GET:
        promocion = serializers.serialize("json",
                                     Promocion.objects.filter(
                                         nombre__icontains=request.GET['id']))
    else:
        promocion = serializers.serialize("json", Promocion.objects.all())
    res = HttpResponse(promocion, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_promocion(req, id):
    promocion = Promocion.objects.filter(id=id).first()
    return JsonResponse({
        'id': promocion.id,
        'descripcion': promocion.descripcion,
        'fecha_inicio': promocion.fecha_inicio,
        'fecha_final': promocion.fecha_final,
        'sucursal': promocion.sucursal,
    })


def crear_promocion(req):
    errores = []
    exito = True
    try:
        nueva_promocion = Promocion()
        nueva_promocion.descripcion = req.POST.get('descripcion', None)
        nueva_promocion.fecha_inicio = req.POST.get('fecha_inicio', None)
        nueva_promocion.fecha_final = req.POST.get('fecha_final', None)
        nueva_promocion.sucursal = req.POST.get('sucursal', None)
        nueva_promocion.full_clean()
        nueva_promocion.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_promocion(req, id):
    errores = []
    exito = True
    try:
        promocion = Promocion.objects.filter(id=id).first()
        promocion.descripcion = req.POST.get('descripcion', '')
        promocion.fecha_inicio = req.POST.get('fecha_inicio', '')
        promocion.fecha_final = req.POST.get('fecha_final', '')
        promocion.sucursal = req.POST.get('sucursal', '')
        promocion.full_clean()
        promocion.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })