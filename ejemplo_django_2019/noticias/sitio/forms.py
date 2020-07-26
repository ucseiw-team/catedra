from django import forms
from sitio.models import Noticia


class FormEjemplo(forms.Form):
    titulo = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=1000)
    fecha = forms.DateTimeField()
    archivada = forms.BooleanField()


class ModelFormEjemplo(forms.ModelForm):
    paparulo = forms.CharField(max_length=200)
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'fecha', 'archivada']
