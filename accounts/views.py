from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    print(user)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login com sucesso.')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def cadastro(request):

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha \
            or not senha2:
        messages.error(request, 'Nenhum campo pode ser vazio')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)

    except:
        messages.error(request, 'Email inválido')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caraceteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 5:
        messages.error(request, 'Usuário precisa ter 6 caraceteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não confere')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso! faça login')
    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
