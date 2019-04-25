from django.shortcuts import render


def login(request):
    return render(request, 'usuario/login.html')


def inicio(request):
    return render(request, 'index.html')


def formularioRegistro(request):
    return render(request, 'usuario/registro_usuario.html')