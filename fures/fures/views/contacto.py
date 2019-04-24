from django.http import HttpResponse, JsonResponse
from django.conf import settings
from ..models import *
from django.core.exceptions import ValidationError
from django.core.mail import send_mail



def crear_msj_contacto(req):
    errores = []
    exito = True
    try:


        nombre = req.POST.get('nombre', None)
        correo = req.POST.get('correo', None)
        telefono = req.POST.get('telefono', None)
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from]
        mensaje_email = req.POST.get('comentario', None) + "\n \n"+"Mis contactos: " + "correo: " + correo +"\n" + "Telefono: "+telefono
        # nueva_contacto.full_clean()
        send_mail(
            nombre,
            mensaje_email,
            email_from,
            [email_to],
            fail_silently=False,
        )


    except ValidationError as e:
        errores = e.messages
        exito = False
    return JsonResponse({
        'exito': exito,
        'errores': errores
    })


