from django import forms
from sitio.models import Noticia


class FormNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = []
