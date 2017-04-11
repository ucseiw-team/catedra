from django.http import JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime

from sitio.models import Noticia
from sitio.forms import LoginForm, NoticiaForm


def inicio(request):
    # nueva = Noticia()
    # nueva.titulo = 'entro alguien!'
    # nueva.texto = 'acaba de entrar alguien al sitio'
    # nueva.fecha = datetime.now()
    # nueva.save()

    noticias = Noticia.objects.all()[:3]

    return render(request, 'inicio.html', {'lista_noticias': noticias})


def acerca_de(request):
    return render(request, 'acerca_de.html', {})


def login_fake(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            return redirect('/inicio/')

    else:
        login_form = LoginForm()

    return render(request, 'login_fake.html', {'form': login_form})


def crear_noticia(request):
    if request.method == 'POST':
        noticia_form = NoticiaForm(request.POST)

        if noticia_form.is_valid():
            noticia = noticia_form.save(commit=False)
            noticia.fecha = datetime.now()
            noticia.save()

            return redirect('/inicio/')

    else:
        noticia_form = NoticiaForm()

    return render(request, 'crear_noticia.html', {'form': noticia_form})


def lista_noticias_ajax(request):
    noticias = Noticia.objects.order_by('-fecha')[:3]

    return render(request, 'lista_noticias.html', {'lista_noticias': noticias})


def contador_noticias_ajax(request):
    datos = {
        'cantidad_noticias': Noticia.objects.count(),
        'cantidad_noticias_archivadas': Noticia.objects.filter(archivada=True).count(),
    }
    return JsonResponse(datos)
