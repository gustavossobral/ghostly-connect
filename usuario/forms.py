from django import forms
from . import models

class UsuarioForm(forms.ModelForm):
    senha2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = models.Usuario
        fields = ['nome', 'username', 'data_nascimento', 'cpf', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput())