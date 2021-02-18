from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    context = {}
    return render(request, 'index.html', context)


def registrar(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Conta {user} criada com sucesso')
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'registrar.html', context)


def logar(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Usuário ou senha incorreto(s)')
    return render(request, 'login.html')


def logout_user(request):
    return redirect('index')
