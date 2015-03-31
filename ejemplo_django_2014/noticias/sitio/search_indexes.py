from haystack import indexes
from models import Noticia


class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name='noticia_text.html')
    titulo = indexes.CharField(model_attr='titulo')
    fecha = indexes.DateTimeField(model_attr='fecha')

    def get_model(self):
        return Noticia

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
