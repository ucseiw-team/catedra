from django.shortcuts import render
from django.http import JsonResponse

from sitio.models import Noticia
from datetime import datetime


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.all()
    return render(request, 'sitio/inicio.html', {'lista_noticias': noticias})


def novedades(request):
    novedad = "Hay muchos crimenes"
    return render(request, 'sitio/novedades.html', {'novedad': novedad})


def contador_ajax(request):
    return JsonResponse({'contador': Noticia.objects.count()})


def titulos_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'sitio/titulos_noticias.html', {'noticias': noticias})
