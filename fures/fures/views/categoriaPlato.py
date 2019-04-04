from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_categoriasPlato(request):
    if 'descripcion' in request.GET:
        categoriaPlato = serializers.serialize("json",
                                     CategoriaPlato.objects.filter(
                                         nombre__icontains=request.GET['descripcion']))
    else:
        categoriaPlato = serializers.serialize("json", CategoriaPlato.objects.all())
    res = HttpResponse(categoriaPlato, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_categoriaPlato(req, id):
    categoriaPlato = CategoriaPlato.objects.filter(id=id).first()
    return JsonResponse({
        'id': categoriaPlato.id,
        'descripcion': categoriaPlato.descripcion
    })


def crear_categoriaPlato(req):
    errores = []
    exito = True
    try:
        nueva_categoriaPlato = CategoriaPlato()
        nueva_categoriaPlato.descripcion = req.POST.get('descripcion', None)
        nueva_categoriaPlato.full_clean()
        nueva_categoriaPlato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_categoriaPlato(req, id):
    errores = []
    exito = True
    try:
        categoriaPlato = CategoriaPlato.objects.filter(id=id).first()
        categoriaPlato.descripcion = req.POST.get('descripcion', '')
        categoriaPlato.full_clean()
        categoriaPlato.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })