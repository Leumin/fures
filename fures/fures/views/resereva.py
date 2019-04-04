from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_reservas(request):
    if 'id' in request.GET:
        reserva = serializers.serialize("json",
                                     Reserva.objects.filter(
                                         nombre__icontains=request.GET['id']))
    else:
        reserva = serializers.serialize("json", Reserva.objects.all())
    res = HttpResponse(reserva, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_reserva(req, id):
    reserva = Reserva.objects.filter(id=id).first()
    return JsonResponse({
        'id': reserva.id,
        'hora_fecha_reserva': reserva.hora_fecha_reserva,
        'estado_reserva': reserva.estado_reserva,
        'cantidad_personas': reserva.cantidad_personas,
        'sucursal': reserva.sucursal,
        'usuario': reserva.usuario,
        'motivo_cancelacion': reserva.motivo_cancelacion
    })


def crear_reserva(req):
    errores = []
    exito = True
    try:
        nueva_reserva = Reserva()
        nueva_reserva.hora_fecha_reserva = req.POST.get('hora_fecha_reserva', None)
        nueva_reserva.estado_reserva = req.POST.get('estado_reserva', None)
        nueva_reserva.cantidad_personas = req.POST.get('cantidad_personas', None)
        nueva_reserva.sucursal = req.POST.get('sucursal', None)
        nueva_reserva.usuario = req.POST.get('usuario', None)
        nueva_reserva.motivo_cancelacion = req.POST.get('motivo_cancelacion', None)
        nueva_reserva.full_clean()
        nueva_reserva.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_reserva(req, id):
    errores = []
    exito = True
    try:
        reserva = Reserva.objects.filter(id=id).first()
        reserva.hora_fecha_reserva = req.POST.get('hora_fecha_reserva', '')
        reserva.estado_reserva = req.POST.get('estado_reserva', '')
        reserva.cantidad_personas = req.POST.get('cantidad_personas', '')
        reserva.sucursal = req.POST.get('sucursal', '')
        reserva.usuario = req.POST.get('usuario', '')
        reserva.motivo_cancelacion = req.POST.get('motivo_cancelacion', '')
        reserva.full_clean()
        reserva.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })