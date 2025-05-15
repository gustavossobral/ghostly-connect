from django import forms
from . import models

class PostagemForm(forms.ModelForm):
    class Meta:
        model = models.Postagens
        fields = ['titulo', 'conteudo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = models.Comentarios
        fields = ['conteudo']