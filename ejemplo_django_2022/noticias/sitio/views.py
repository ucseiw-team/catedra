from django.shortcuts import render, HttpResponseRedirect
from sitio.models import Noticia
from datetime import datetime

from sitio.forms import FormularioNoticia, FormularioModeloNoticia



def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.filter(archivada=False).order_by("fecha")

    return render(
        request,
        'inicio.html',
        {'lista_noticias': noticias},
    )


def ejemplo_form_pelado(request):
    print("los datos son:", request.POST)
    return render(request, "ejemplo_form_pelado.html", {})


def ejemplo_form_django(request):
    if request.method == "POST":
        form = FormularioNoticia(request.POST)

        if form.is_valid():
            print("los datos finales son:", form.cleaned_data)
            return HttpResponseRedirect("/inicio/")
    else:
        form = FormularioNoticia()

    return render(request, "ejemplo_form_django.html", {"form": form})


def ejemplo_model_form_django(request):
    if request.method == "POST":
        form = FormularioModeloNoticia(request.POST)
        if form.is_valid():
            form.save()  # esto crea y guarda la noticia!
            return HttpResponseRedirect("/inicio/")
    else:
        form = FormularioModeloNoticia()

    return render(request, "ejemplo_form_django.html", {"form": form})  # podemos seguir usando el mismo template que con el form normal :)
