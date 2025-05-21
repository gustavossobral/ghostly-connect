from django. urls import path
from . import views

urlpatterns = [
    path('<int:postagem_id>', views.reportar_postagem, name='reportar_postagem'),
]
