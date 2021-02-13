from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)


def registrar(request):
    context = {}
    return render(request, 'registrar.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)
