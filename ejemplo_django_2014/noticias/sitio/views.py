# coding: utf-8
from datetime import datetime
from django.shortcuts import render
from sitio.models import Noticia, Categoria
from django.http import HttpResponse, HttpResponseRedirect
from api import crear_policial
from forms import FormNoticia

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


def crear_noticia_policial(request):
    nueva = crear_policial()
    return render(request, 'crear_noticia_policial.html', {'noticia': nueva})


def crear_noticia_con_datos(request):
    if request.method == 'GET':
        # me estan pidiendo la pagina vacia
        # para escribir los datos
        form = FormNoticia()
    else:
        # me estan mandando los datos que
        # tengo que guardar
        form = FormNoticia(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio/')

    return render(request,
                  'crear_noticia_con_datos.html',
                  {'form_noticia': form})
