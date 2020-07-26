from django.http import HttpResponseRedirect
from django.shortcuts import render
from sitio.models import Noticia
from datetime import datetime

from sitio.forms import FormEjemplo, ModelFormEjemplo


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.all()
    return render(request, 'inicio.html', {'lista_noticias': noticias})


def ejemplo_form(request):
    print('En GET vino:', request.GET)
    print('En POST vino:', request.POST)
    return render(request, 'ejemplo_form.html', {})


def ejemplo_form_copado(request):
    if request.method == "POST":
        form = FormEjemplo(request.POST)

        if form.is_valid():
            print(form.cleaned_data['titulo'])
            return HttpResponseRedirect('/inicio/')
    else:
        form = FormEjemplo()

    return render(request, 'ejemplo_form_copado.html', {'form': form})


def ejemplo_model_form(request):
    if request.method == "POST":
        form = ModelFormEjemplo(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio/')
    else:
        form = ModelFormEjemplo()

    return render(request, 'ejemplo_form_copado.html', {'form': form})
