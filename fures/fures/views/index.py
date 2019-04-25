from django.shortcuts import render


def inicio(request):
    return render(request, 'administrador/admin_index.html')


def login(request):
    return render(request, 'administrador/admin_index.html')


def formularioRegistro(request):
    return render(request, 'usuario/registro_usuario.html')