from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    archivada = models.BooleanField(default=False)
    fecha = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, blank=True, null=True)

    def __unicode__(self):
        return self.titulo
