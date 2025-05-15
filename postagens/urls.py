from django.urls import path
from . import views

urlpatterns = [
    path('postar/', views.postar, name='postar'),
    path('postagem/<int:postagem_id>/', views.visualizar_postagem, name='visualizar_postagem'),
    path('enviar_comentario/<int:postagem_id>/', views.enviar_comentario, name='enviar_comentario'),
]

