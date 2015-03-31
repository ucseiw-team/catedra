from django.shortcuts import render

from sitio.models import Noticia
from datetime import datetime


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    a = 1/0

    noticias = Noticia.objects.all()
    return render(request, 'inicio.html', {'lista_noticias': noticias})


