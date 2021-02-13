from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def index(request):
    context = {}
    return render(request, 'index.html', context)


def registrar(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'registrar.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)
