from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_usuarios(request):
    if 'nombre' in request.GET:
        usuario = serializers.serialize("json",
                                     Usuario.objects.filter(
                                         nombre__icontains=request.GET['nombre']))
    else:
        usuario = serializers.serialize("json", Usuario.objects.all())
    res = HttpResponse(usuario, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_usuario(req, id):
    usuario = Usuario.objects.filter(id=id).first()
    return JsonResponse({
        'id': usuario.id,
        'nombre_persona': usuario.nombre_persona,
        'apellido_persona': usuario.apellido_persona,
        'direccion': usuario.direccion,
        'nombre_usuario': usuario.nombre_usuario,
        'contrasena': usuario.contrasena,
        'correo': usuario.correo,
        'telefono': usuario.telefono
    })


def crear_usuario(req):
    errores = []
    exito = True
    try:
        nuevo_usuario = Usuario()
        nuevo_usuario.nombre_persona = req.POST.get('nombre_persona', None)
        nuevo_usuario.apellido_persona = req.POST.get('apellido_persona', None)
        nuevo_usuario.direccion = req.POST.get('direccion', None)
        nuevo_usuario.nombre_usuario = req.POST.get('nombre_usuario', None)
        nuevo_usuario.contrasena = req.POST.get('contrasena', None)
        nuevo_usuario.correo = req.POST.get('correo', None)
        nuevo_usuario.telefono = req.POST.get('telefono', None)
        nuevo_usuario.full_clean()
        nuevo_usuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_usuario(req, id):
    errores = []
    exito = True
    try:
        usuario = Usuario.objects.filter(id=id).first()
        usuario.nombre_persona = req.POST.get('nombre_persona', '')
        usuario.apellido_persona = req.POST.get('apellido_persona', '')
        usuario.direccion = req.POST.get('direccion', '')
        usuario.nombre_usuario = req.POST.get('nombre_usuario', '')
        usuario.contrasena = req.POST.get('contrasena', '')
        usuario.correo = req.POST.get('correo', '')
        usuario.telefono = req.POST.get('telefono', '')
        usuario.full_clean()
        usuario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })