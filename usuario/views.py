from django.shortcuts import render, redirect
from . import models
from validate_docbr import CPF
from django.contrib.auth.models import User
from . import forms
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = forms.LoginForm(request.POST)
    error_message = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            senha = form.cleaned_data['senha']
            user = authenticate(request, username=username, password=senha)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Nome de usuário ou senha inválidos. Por favor, tente novamente.'
            
    return render(request, 'auth/login.html', {'error_message': error_message})

def cadastro_view(request):
    cpf_validator = CPF()
    form = forms.UsuarioForm(request.POST)
    error_message = None
    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome'].title()
            username = form.cleaned_data['username']
            data_nascimento = form.cleaned_data['data_nascimento']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            senha2 = request.POST.get('senha2', '').strip()

            hoje = datetime.today()
            idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
            
            if not nome:
                error_message = 'O campo Nome Completo é obrigatório.'
            elif not cpf_validator.validate(cpf):
                error_message = 'CPF inválido. Por favor, insira um CPF válido.'
            elif User.objects.filter(username=username).exists():
                error_message = 'Nome de usuário já existe. Por favor, escolha outro.'
            elif User.objects.filter(email=email).exists():
                error_message = 'Email já existe. Por favor, escolha outro.'
            elif senha != senha2:
                error_message = 'As senhas não coincidem. Por favor, tente novamente.'
            elif idade < 18:
                error_message = 'Você deve ter mais de 18 anos para se cadastrar.'
            else:
                user = User.objects.create_user(
                    username=username,
                    password=senha,
                    first_name=nome,
                    email=email
                )
                user.save()
                usuario_model = models.Usuario(
                    nome=nome,
                    username=username,
                    data_nascimento=data_nascimento,
                    cpf=cpf,
                    email=email,
                    senha=senha,
                )
                usuario_model.save()
                return render(request, 'auth/login.html')

    return render(request, 'auth/cadastro.html', {'form': form, 'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')