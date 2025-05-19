from django.shortcuts import render, redirect
from postagens.models import Postagens, Comentarios

def home(request):
    error_message = None
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    postagens = Postagens.objects.all().order_by('data_postagem')
    return render(request, 'home/home.html', {'error_message': error_message,'postagens': postagens})
