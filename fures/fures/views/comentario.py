from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_comentarios(request):
    if 'id' in request.GET:
        comentario = serializers.serialize("json",
                                     Comentario.objects.filter(
                                         nombre__icontains=request.GET['id']))
    else:
        comentario = serializers.serialize("json", Comentario.objects.all())
    res = HttpResponse(comentario, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_comentario(req, id):
    comentario = Comentario.objects.filter(id=id).first()
    return JsonResponse({
        'sucursal': comentario.unique_together,
        'usuario': comentario.unique_together,
        'comentario': comentario.comentario,
        'puntuacion': comentario.puntuacion,
    })


def crear_comentario(req):
    errores = []
    exito = True
    try:
        nuevo_comentario = Comentario()
        nuevo_comentario.sucursal_id = req.POST.get('sucursal', None)
        nuevo_comentario.usuario_id = req.POST.get('usuario', None)
        nuevo_comentario.comentario = req.POST.get('comentario', None)
        nuevo_comentario.puntuacion = req.POST.get('star', None)
        nuevo_comentario.full_clean()
        nuevo_comentario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_comentario(req, id):
    errores = []
    exito = True
    try:
        comentario = Comentario.objects.filter(id=id).first()
        comentario.sucursal_id = req.POST.get('sucursal', '')
        comentario.usuario_id = req.POST.get('usuario', '')
        comentario.comentario = req.POST.get('comentario', '')
        comentario.puntuacion = req.POST.get('puntuacion', '')
        # comentario.full_clean()
        comentario.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })