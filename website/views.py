from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html', {})

def quero_trabalhar(request):
    return render(request, 'website/quero_trabalhar.html', {})

def quero_trabalhar_design(request):
    return render(request, 'website/quero_trabalhar_design.html', {})

def quero_trabalhar_programacao(request):
    return render(request, 'website/quero_trabalhar_programacao.html', {})

def quero_trabalhar_negocios(request):
    return render(request, 'website/quero_trabalhar_negocios.html', {})

def terminando(request):
    return render(request, 'website/terminando.html', {})

def quero_contratar(request):
    return render(request, 'website/quero_contratar.html', {})

def sobre_vc(request):
    return render(request, 'website/sobre_vc.html', {})

def completa_perfil(request):
    return render(request, 'website/completa_perfil.html', {})

def procura_trampo(request):
    return render(request, 'website/procura_trampo.html', {})


