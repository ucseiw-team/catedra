# coding: utf-8
from datetime import datetime
from django.shortcuts import render
from sitio.models import Noticia


def ejemplo_clase_1(request):
    '''Este es un ejemplo bastante básico de una vista con datos sacados de
    la base de datos.'''

    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.all()

    return render(request, 'ejemplo_clase_1.html', {'lista_noticias': noticias})


def ejemplo_clase_2(request):
    '''Este es un ejemplo básico de html con css y javascript.'''
    return render(request, 'ejemplo_clase_2.html', {})
