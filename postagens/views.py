from django.shortcuts import render, redirect
from .forms import PostagemForm, ComentarioForm
from .models import Postagens, Comentarios
from django.shortcuts import get_object_or_404

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

def visualizar_postagem(request, postagem_id):
    error_message = None
    post = get_object_or_404(Postagens, id=postagem_id)
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    
    comentarios = post.comentarios_set.all()
    return render(request, 'postagens/post.html', {'post': post, 'error_message': error_message,'comentarios': comentarios})

def enviar_comentario(request, postagem_id):
    error_message = None
    post = get_object_or_404(Postagens, id=postagem_id)
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    
    if request.method == 'POST':    
        form = ComentarioForm(request.POST)
        if form.is_valid():
            conteudo = form.cleaned_data['conteudo']
            comentario = Comentarios.objects.create(
                postagem=post,
                autor=request.user,
                conteudo=conteudo
            )
            comentario.save()
            return redirect('visualizar_postagem', postagem_id=postagem_id)
        else:
            error_message = 'Erro ao enviar comentário. Verifique os campos e tente novamente.'
    else:
        form = ComentarioForm()
    return render(request, 'postagens/post.html', {'post': post, 'form': form, 'error_message': error_message})
    
