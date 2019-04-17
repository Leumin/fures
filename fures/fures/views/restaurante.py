from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render

from ..models import *

from django.core.exceptions import ValidationError


def restauranteshtml(request):
    return render(request, 'usuario/restaurantes.html')



def ver_restaurantes(request):
    if 'nombre' in request.GET:
        restaurante = serializers.serialize("json",
                                     Restaurante.objects.filter(
                                         nombre__icontains=request.GET['nombre']))
    else:
        restaurante = serializers.serialize("json", Restaurante.objects.all())
    res = HttpResponse(restaurante, content_type="application/json")
    res['Access-Control-Allow-Origin'] = '*'
    return res


def ver_restaurante(req, id):
    restaurante = Restaurante.objects.filter(id=id).first()
    return JsonResponse({
        'id': restaurante.id,
        'nombre': restaurante.nombre,
        'descripcion': restaurante.descripcion,
        'imagen': restaurante.imagen,
        'estado': restaurante.estado
    })


def crear_restaurante(request):
    errores = []
    exito = True
    try:
        if request.method == 'POST':
            nuevo_restaurante = Restaurante()
            nuevo_restaurante.nombre = request.POST.get('nombre', None)
            nuevo_restaurante.descripcion = request.POST.get('descripcion', None)
            nuevo_restaurante.imagen = request.FILES['imagen']
            nuevo_restaurante.estado = request.POST.get('estado', None)
            nuevo_restaurante.full_clean()
            nuevo_restaurante.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


def actualizar_restaurante(req, id):
    errores = []
    exito = True
    try:
        restaurante = Restaurante.objects.filter(id=id).first()
        restaurante.nombre = req.POST.get('nombre', '')
        restaurante.descripcion = req.POST.get('descripcion', '')
        restaurante.estado = req.POST.get('estado', '')
        restaurante.full_clean()
        restaurante.save()
    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })