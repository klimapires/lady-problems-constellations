from django.shortcuts import render, redirect

from website.forms import JobPostForm

from website.models import JobCategory, JobPost

def index(request):
    return render(request, 'website/index.html', {})

def quero_trabalhar(request):
    if request.method == 'POST':
        areas = request.POST.getlist('areas')
        request.session['quero-trabalhar-areas'] = areas

        return redirect('terminando')
    else:
        request.session['quero-trabalhar'] = True

        categories = JobCategory.objects.all()

        return render(request, 'website/quero_trabalhar.html', {'categories': categories})

def quero_trabalhar_areas(request, slug):
    request.session['quero-trabalhar-categoria'] = slug

    category = JobCategory.objects.get(slug=slug)
    areas = category.jobarea_set.all()
    return render(request, 'website/quero_trabalhar_areas.html', {'category': category, 'areas': areas})

def busca_vagas(request):
    areas = []

    session_areas = request.session.get('quero-trabalhar-areas')
    if isinstance(session_areas, list):
        areas.extend(session_areas)

    query_areas = request.GET.getlist('areas')
    if isinstance(query_areas, list):
        areas.extend(query_areas)

    jobs = JobPost.objects.filter_by_areas(areas)

    return render(request, 'website/busca_vagas.html', {'jobs': jobs})

def terminando(request):
    return render(request, 'website/terminando.html', {})

def quero_contratar(request):
    request.session['quero-contratar'] = True

    categories = JobCategory.objects.all()

    return render(request, 'website/quero_contratar.html', {'categories': categories})

def quero_contratar_areas(request, slug):
    request.session['quero-contratar-areas'] = slug

    category = JobCategory.objects.get(slug=slug)
    areas = category.jobarea_set.all()
    return render(request, 'website/quero_contratar_areas.html', {'category': category, 'areas': areas})

def contrato_sobre_vc(request):
    return render(request, 'website/contrato_sobre_vc.html', {})

def completa_perfil(request):
    return render(request, 'website/completa_perfil.html', {})

def busca_vagas(request):
    return render(request, 'website/busca_vagas.html', {})

def cadastra_trabalho(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-trabalhos')
    else:
        form = JobPostForm()

    return render(request, 'website/cadastra_trabalho.html', {'form': form})

def contrata_alteraperfil (request):
    return render(request, 'website/contrata_alteraperfil.html', {})

def contrata_buscapessoa(request):
    return render(request, 'website/contrata_buscapessoa.html', {})

def contrata_criajob(request):
    return render(request, 'website/contrata_criajob.html', {})

def contrata_historico(request):
    return render(request, 'website/contrata_historico.html', {})

def contrata_pagamento(request):
    return render(request, 'website/contrata_pagamento.html', {})

def contrata_projeto(request):
    return render(request, 'website/contrata_projeto.html', {})