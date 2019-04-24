from django.shortcuts import render


def inicio_admin(request):
    return render(request, 'administrador/crear_sucursal.html')
