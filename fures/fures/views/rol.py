from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_roles(request):
    if 'descripcion' in request.GET:
        rol = serializers.serialize("json",
                                     Rol.objects.filter(
                                         nombre__icontains=request.GET['descripcion']))
    else:
        rol = serializers.serialize("json", Rol.objects.all())
    res = HttpResponse(rol, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_rol(req, id):
    rol = Rol.objects.filter(id=id).first()
    return JsonResponse({
        'id': rol.id,
        'descripcion': rol.descripcion
    })


def crear_rol(req):
    errores = []
    exito = True
    try:
        nuevo_rol = Rol()
        nuevo_rol.descripcion = req.POST.get('descripcion', None)
        nuevo_rol.full_clean()
        nuevo_rol.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_rol(req, id):
    errores = []
    exito = True
    try:
        rol = Rol.objects.filter(id=id).first()
        rol.descripcion = req.POST.get('descripcion', '')
        rol.full_clean()
        rol.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })