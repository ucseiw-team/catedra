from django import forms
from models import Noticia


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'archivada', 'categoria']
