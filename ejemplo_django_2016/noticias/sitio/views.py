from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from sitio.models import Noticia, Categoria
from sitio.forms import FormNoticia
from datetime import datetime


def inicio(request):
    policiales = Categoria.objects.get(nombre='policiales')
    noticias = policiales.noticia_set.filter(archivada=False).order_by('fecha')
    return render(request, 'inicio.html', {'lista_noticias': noticias})


def pedir_datos(request):
    if request.method == "GET":
        mi_form = FormNoticia()
    else:
        mi_form = FormNoticia(request.POST)
        if mi_form.is_valid():
            mi_form.save()
            return HttpResponseRedirect('/inicio/')

    return render(request, 'pedir_datos.html', {'form_noticia': mi_form})


def inicio_ajax(request):
    return render(request, 'inicio_ajax.html', {})


def lista_noticias_ajax(request):
    noticias = Noticia.objects.all().order_by('fecha')
    return render(request, 'lista_noticias.html', {'lista_noticias': noticias})


def contador_noticias_ajax(request):
    resultado = {"cantidad": Noticia.objects.all().count()}
    return JsonResponse(resultado)
