from django.shortcuts import render


def inicio_admin(request):
    return render(request, 'administrador/modificar_sucursal.html')

def sucursal(request):
    return render(request, 'administrador/modificar_sucursal.html')

def Visualizar_sucursal(request):
    return render(request, 'administrador/visualizar_sucursales.html')

def Crear_Plato(request):
    return render(request, 'administrador/crear_platos.html')

def Visualizar_Plato(request):
    return render(request, 'administrador/visualizar_platos.html')

def crear_sucursales_html(request):
    return render(request, 'administrador/crear_sucursal.html')

def Crear_Servicios(request):
    return render(request, 'administrador/crear_servicios.html')

