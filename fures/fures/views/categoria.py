from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_categorias(request):
    if 'descripcion' in request.GET:
        cats = serializers.serialize("json",
                                     Categoria.objects.filter(
                                         nombre__icontains=request.GET['descripcion']))
    else:
        cats = serializers.serialize("json", Categoria.objects.all())
    res = HttpResponse(cats, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_categoria(req, id):
    categoria = Categoria.objects.filter(id=id).first()
    return JsonResponse({
        'id': categoria.id,
        'descripcion': categoria.descripcion
    })


def crear_categoria(req):
    errores = []
    exito = True
    try:
        nueva_categoria = Categoria()
        nueva_categoria.descripcion = req.POST.get('descripcion', None)
        nueva_categoria.full_clean()
        nueva_categoria.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_categoria(req, id):
    errores = []
    exito = True
    try:
        cat = Categoria.objects.filter(id=id).first()
        cat.descripcion = req.POST.get('descripcion', '')
        cat.full_clean()
        cat.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })

