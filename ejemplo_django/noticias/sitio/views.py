# coding: utf-8
from datetime import datetime
from django.shortcuts import render
from sitio.models import Noticia
from django.http import HttpResponse

import json


def inicio(request):
    '''Este es un ejemplo bastante básico de una vista con datos sacados de
    la base de datos.'''

    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.all()

    return render(request, 'inicio.html', {'lista_noticias': noticias})


def contador(request):
    '''Este es un ejemplo básico de html con css y javascript.'''
    return render(request, 'contador.html')


def vacia(request):
    '''Este es un ejemplo con template que no define bloques.'''
    return render(request, 'vacia.html')


def contador_ajax(request):
    '''Este es un ejemplo básico peticiones ajax.'''
    return render(request, 'contador_ajax.html')


def sumar_numero(request, numero):
    '''Esta es una vista que recibe un numero y devuelve n+1.'''
    numero = int(numero) + 1
    return render(request, 'sumar_numero.html', {'numero': numero})


def sumar_numero_json(request, numero):
    '''Esta es una vista que recibe un numero y devuelve n+1, pero en json.'''
    numero = int(numero) + 1
    datos = {'numero': numero,
             'texto': 'hola mundo'}
    return HttpResponse(json.dumps(datos))
