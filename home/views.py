from django.shortcuts import render, redirect, get_object_or_404
from postagens.models import Postagens

def home(request):
    error_message = None
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    postagens = Postagens.objects.all().order_by('-data_postagem')
    return render(request, 'home/home.html', {'error_message': error_message,'postagens': postagens})

def suas_publicacoes(request):
    error_message = None
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    postagens = Postagens.objects.filter(autor=request.user).order_by('-data_postagem')
    return render(request, 'home/userposts.html', {'error_message': error_message,'postagens': postagens})

def excluir_postagem(request, post_id):
    postagem = get_object_or_404(Postagens, id=post_id)
    postagem.delete()      
    return redirect('home')
    