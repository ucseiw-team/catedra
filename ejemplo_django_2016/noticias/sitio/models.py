from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    archivada = models.BooleanField(default=False)
    lugar = models.CharField(max_length=50, default='Aca')
    categoria = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return self.titulo
