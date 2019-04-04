from django.http import HttpResponse, JsonResponse
from django.core import serializers
from ..models import *
from django.core.exceptions import ValidationError


def ver_menus(request):
    if 'nombre_menu' in request.GET:
        menu = serializers.serialize("json",
                                     Menu.objects.filter(
                                         nombre__icontains=request.GET['nombre_menu']))
    else:
        menu = serializers.serialize("json", Menu.objects.all())
    res = HttpResponse(menu, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_menu(req, id):
    menu = Menu.objects.filter(id=id).first()
    return JsonResponse({
        'id': menu.id,
        'nombre': menu.nombre_menu,
        'descripcion': menu.descripcion,
    })


def crear_menu(req):
    errores = []
    exito = True
    try:
        nuevo_menu = Restaurante()
        nuevo_menu.nombre_menu = req.POST.get('nombre', None)
        nuevo_menu.descripcion = req.POST.get('descripcion', None)
        nuevo_menu.full_clean()
        nuevo_menu.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_menu(req, id):
    errores = []
    exito = True
    try:
        res = Restaurante.objects.filter(id=id).first()
        res.nombre_menu = req.POST.get('nombre_menu', '')
        res.descripcion = req.POST.get('descripcion', '')
        res.full_clean()
        res.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })