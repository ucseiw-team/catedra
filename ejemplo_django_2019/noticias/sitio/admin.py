from django.contrib import admin
from sitio.models import Noticia


class AdminNoticia(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha',)
    list_filter = ('archivada', 'fecha')
    search_fields = ('texto', )
    date_hierarchy = 'fecha'


admin.site.register(Noticia, AdminNoticia)
