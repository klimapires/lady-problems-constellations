from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html', {})

def quero_trabalhar(request):
    return render(request, 'website/quero_trabalhar.html', {})

def quero_contratar(request):
    return render(request, 'website/quero_contratar.html', {})

def procura_trampo(request):
    return render(request, 'website/procura_trampo.html', {})