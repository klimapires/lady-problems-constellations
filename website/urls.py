from django.conf.urls import url, include

from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^quero-trabalhar/$', views.quero_trabalhar, name='quero-trabalhar'),
    url(r'^quero-trabalhar/(?P<slug>[-\w]+)/$', views.quero_trabalhar_areas, name='quero-trabalhar-areas'),

    url(r'^quero-contratar/$', views.quero_contratar, name='quero-contratar'),
    url(r'^terminando/$', views.terminando, name='terminando'),
    url(r'^completa-perfil/$', views.completa_perfil, name='completa-perfil'),
    url(r'^sobre-vc/$', views.sobre_vc, name='sobre-vc'),
    url(r'^procurar-trampo/$', views.procura_trampo, name='procurar-trampo'),

    url(r'', include('django.contrib.auth.urls')),
]
