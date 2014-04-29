from models import Noticia, Categoria
from datetime import datetime


def crear_policial():
    nueva = Noticia()
    nueva.titulo = 'nueva policial'
    nueva.texto = 'escriba aqui su noticia policial'
    nueva.fecha = datetime.now()
    nueva.categoria = Categoria.objects.get(nombre='policiales')
    nueva.save()

    return nueva
