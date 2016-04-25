from django.contrib import admin
from sitio.models import Noticia, Categoria


class AdminNoticia(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha',)
    list_filter = ('archivada', 'fecha', 'categoria')
    search_fields = ('texto', )
    date_hierarchy = 'fecha'


class AdminCategoria(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('descripcion', )



admin.site.register(Noticia, AdminNoticia)
admin.site.register(Categoria, AdminCategoria)
