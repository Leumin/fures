from django.shortcuts import render


def inicio(request):
    return render(request, 'administrador/crear_sucursal.html')


def login(request):
    return render(request, 'usuario/login.html')


def formularioRegistro(request):
    return render(request, 'usuario/registro_usuario.html')