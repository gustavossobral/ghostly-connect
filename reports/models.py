from django.db import models
from postagens.models import Postagens

class Report(models.Model):
    motivo = models.CharField(max_length=1000)
    data = models.DateField(auto_now_add=True)
    postagem = models.ForeignKey(Postagens, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.postagem} - {self.motivo}'