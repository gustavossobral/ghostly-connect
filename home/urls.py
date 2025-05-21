from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('suas_publicacoes/', views.suas_publicacoes, name='suas_publicacoes'),
    path('excluir_postagem/<int:postagem_id>/', views.excluir_postagem, name='excluir_postagem'),
]
