from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    cpf = models.CharField(max_length=14, unique=True, default='', blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    senha = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome
