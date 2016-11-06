from django.shortcuts import render, redirect

from website.forms import JobPostForm

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

def quero_contratar(request):
    return render(request, 'website/quero_contratar.html', {})

def cadastra_trabalho(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-trabalhos')
    else:
        form = JobPostForm()

    return render(request, 'website/cadastra_trabalho.html', {'form': form})
