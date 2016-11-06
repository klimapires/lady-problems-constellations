import string
import random

from django.contrib.auth import get_user_model
from django.contrib.auth import login as login_user
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect

from website.forms import JobPostForm

from website.models import JobCategory, JobPost, JobArea

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
    query_areas = request.GET.getlist('q', [])

    session_areas = request.session.pop('quero-trabalhar-areas', [])
    if session_areas:
        url = reverse('busca-vagas') + '?' + '&'.join('q={}'.format(q) for q in session_areas + query_areas)
        return redirect(url)

    if not query_areas:
        jobs = JobPost.objects.all()
    else:
        jobs = JobPost.objects.filter_by_areas(query_areas)

    areas = JobArea.objects.filter(id__in=query_areas)

    return render(request, 'website/busca_vagas.html', {'jobs': jobs, 'selected_areas': areas})

def candidatar_vaga(request, id):
    if not request.user.is_authenticated:
        url = reverse("login") + '?next=' + request.path
        messages.info(request, 'Para se candidatar a alguma das vagas, por favor faça login')
        return redirect(url)
    job = JobPost.objects.get(pk=id)
    messages.info(request, 'Candidatou-se à vaga {}'.format(job.title))

    return redirect('busca-vagas')

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

def contrata_sobre_vc(request):
    return render(request, 'website/contrata_sobre_vc.html', {})

def completa_perfil(request):
    if request.method == 'POST':
        username = ''.join(random.sample(string.ascii_letters, 16))
        email = request.POST['email']
        password = request.POST['password']

        User = get_user_model()

        user = User.objects.create_user(
            username,
            email,
            password,
        )

        login_user(request, user)

        return redirect('busca-vagas')
    else:
        return render(request, 'website/completa_perfil.html', {})

def cadastra_trabalho(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-trabalhos')
    else:
        form = JobPostForm()

    return render(request, 'website/cadastra_trabalhos.html', {'form': form})

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

def contrata_criajob(request):
    return render(request, 'website/contrata_criajob.html', {})

