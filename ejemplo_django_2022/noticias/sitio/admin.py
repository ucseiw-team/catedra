from django.contrib import admin

from sitio.models import Noticia, Categoria


@admin.register(Noticia)
class AdminNoticia(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'categoria')
    list_filter = ('archivada', 'fecha', 'categoria')
    search_fields = ('texto', )
    date_hierarchy = 'fecha'

@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ('id', 'nombre')


