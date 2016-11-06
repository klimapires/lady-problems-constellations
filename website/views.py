from django.shortcuts import render, redirect

from website.forms import JobPostForm

from website.models import JobCategory

def index(request):
    return render(request, 'website/index.html', {})

def quero_trabalhar(request):
    categories = JobCategory.objects.all()

    return render(request, 'website/quero_trabalhar.html', {'categories': categories})

def quero_trabalhar_areas(request, slug):
    category = JobCategory.objects.get(slug=slug)
    areas = category.jobarea_set.all()
    return render(request, 'website/quero_trabalhar_areas.html', {'category': category, 'areas': areas})

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

def cadastra_trabalho(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-trabalhos')
    else:
        form = JobPostForm()

    return render(request, 'website/cadastra_trabalho.html', {'form': form})
