from django.conf.urls import url, include

from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^quero-trabalhar/$', views.quero_trabalhar, name='quero-trabalhar'),
    url(r'^quero-trabalhar/design/$', views.quero_trabalhar_design, name='quero-trabalhar-design'),
    url(r'^quero-trabalhar/programacao/$', views.quero_trabalhar_programacao, name='quero-trabalhar-programacao'),
    url(r'^quero-trabalhar/negocios/$', views.quero_trabalhar_negocios, name='quero-trabalhar-negocios'),
    url(r'^quero-contratar/$', views.quero_contratar, name='quero-contratar'),
    url(r'^terminando/$', views.terminando, name='terminando'),
    url(r'^login/$', views.login, name='login'),
]
