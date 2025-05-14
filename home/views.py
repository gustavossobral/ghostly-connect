from django.shortcuts import render, redirect
from .forms import PostagemForm
from .models import Postagens

def home(request):
    error_message = None
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    return render(request, 'home/home.html', {'error_message': error_message})

def postar(request):
    error_message = None
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    
    if request.method == 'POST':
        print(request.POST) 
        form = PostagemForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            conteudo = form.cleaned_data['conteudo']

            post = Postagens.objects.create(
                titulo=titulo,
                conteudo=conteudo,
                autor=request.user
            )
            post.save()

            return redirect('home')
        else:
            print(form.errors)
            error_message = 'Erro ao criar postagem. Verifique os campos e tente novamente.'
    else:
        form = PostagemForm()
    
    return render(request, 'home/home.html', {'error_message': error_message})