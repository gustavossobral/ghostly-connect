from django.db import models
from django.contrib.auth.models import User

class Postagens(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo