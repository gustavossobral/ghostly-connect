from django.shortcuts import render, redirect
from . import models
from validate_docbr import CPF
from django.contrib.auth.models import User
from . import forms
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def login_view(request):
    form = forms.LoginForm(request.POST)
    error_message = None
    if request.method == 'POST':
        print("Método POST detectado. Processando os dados do formulário...")
        if form.is_valid():
            print("Formulário válido. Processando os dados...")
            username = form.cleaned_data['username']
            senha = form.cleaned_data['senha']
            print(f"Username: {username}, Senha: {senha}")
            user = authenticate(request, username=username, password=senha)

            if user is not None:
                print("Usuário autenticado com sucesso.")
                login(request, user)
                return HttpResponse("Login realizado com sucesso!")
            else:
                print("Falha na autenticação. Verifique o nome de usuário e a senha.")
                print(User.objects.all())
                error_message = 'Nome de usuário ou senha inválidos. Por favor, tente novamente.'
        else:
            print("Formulário inválido. Verifique os dados inseridos.")
            
    return render(request, 'auth/login.html')

def cadastro_view(request):
    cpf_validator = CPF()
    form = forms.UsuarioForm(request.POST)
    error_message = None
    if request.method == 'POST':
        if form.is_valid():
            print("Formulário válido. Processando os dados...")
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

def logout(request):
    logout(request)
    return redirect('auth/login.html')