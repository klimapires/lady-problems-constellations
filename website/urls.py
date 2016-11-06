from django.conf.urls import url, include

from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^quero-trabalhar/$', views.quero_trabalhar, name='quero-trabalhar'),
    url(r'^quero-trabalhar/(?P<slug>[-\w]+)/$', views.quero_trabalhar_areas, name='quero-trabalhar-areas'),

    url(r'^busca-vagas/$', views.busca_vagas, name='busca-vagas'),

    url(r'^vaga/(?P<id>[\d]+)/candidatar/$', views.candidatar_vaga, name='candidatar-vaga'),

    url(r'^quero-contratar/$', views.quero_contratar, name='quero-contratar'),
    url(r'^quero-contratar/(?P<slug>[-\w]+)/$', views.quero_contratar_areas, name='quero-contratar-areas'),
    url(r'^terminando/$', views.terminando, name='terminando'),
    url(r'^completa-perfil/$', views.completa_perfil, name='completa-perfil'),
    url(r'^sobre-vc/$', views.contrato_sobre_vc, name='contrato-sobre-vc'),
    url(r'^busca-vagas/$', views.busca_vagas, name='busca-vagas'),	
    url(r'', include('django.contrib.auth.urls')),
]
