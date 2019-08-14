from django.shortcuts import render
from sitio.models import Noticia
from datetime import datetime



def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.all()
    a = 1 / 0
    return render(request, 'inicio.html', {'lista_noticias': noticias})


def ejemplo_form(request):
    print('En GET vino:', request.GET)
    print('En POST vino:', request.POST)
    return render(request, 'ejemplo_form.html', {})
