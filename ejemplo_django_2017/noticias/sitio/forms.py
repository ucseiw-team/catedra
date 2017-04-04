from django import forms

from sitio.models import Noticia


class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, min_length=3)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        if cleaned_data['usuario'] != 'fisa':
            raise forms.ValidationError('Usuario desconocido')


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = ['fecha',]
