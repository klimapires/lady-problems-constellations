from django.conf.urls import url, include

from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quero-trabalhar/$', views.quero_trabalhar, name='quero-trabalhar'),
    url(r'^quero-contratar/$', views.quero_contratar, name='quero-contratar'),
    url(r'^procurar-trampo/$', views.procura_trampo, name='procurar-trampo'),
]
