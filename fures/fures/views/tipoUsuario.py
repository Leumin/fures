from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_tiposUsuario(request):
    if 'descripcion' in request.GET:
        tipoUsuario = serializers.serialize("json",
                                     TipoUsuario.objects.filter(
                                         nombre__icontains=request.GET['descripcion']))
    else:
        tipoUsuario = serializers.serialize("json", TipoUsuario.objects.all())
    res = HttpResponse(tipoUsuario, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_tipoUsuario(req, id):
    tipoUsuario = TipoUsuario.objects.filter(id=id).first()
    return JsonResponse({
        'id': tipoUsuario.id,
        'descripcion': tipoUsuario.descripcion
    })


def crear_tipoUsuario(req):
    errores = []
    exito = True
    try:
        nuevo_tipoUsuario = TipoUsuario()
        nuevo_tipoUsuario.descripcion = req.POST.get('descripcion', None)
        nuevo_tipoUsuario.full_clean()
        nuevo_tipoUsuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_tipoUsuario(req, id):
    errores = []
    exito = True
    try:
        tipoUsuario = TipoUsuario.objects.filter(id=id).first()
        tipoUsuario.descripcion = req.POST.get('descripcion', '')
        tipoUsuario.full_clean()
        tipoUsuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })