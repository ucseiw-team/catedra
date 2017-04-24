from haystack import indexes

from sitio.models import Noticia


class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='titulo')
    fecha = indexes.DateTimeField(model_attr='fecha')

    def get_model(self):
        return Noticia

    def index_queryset(self, using=None):
        """Queremos que se indexen todas las noticias que tengan archivada=False"""
        return self.get_model().objects.filter(archivada=False)
