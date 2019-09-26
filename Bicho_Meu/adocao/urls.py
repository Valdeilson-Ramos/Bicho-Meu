rom django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<adocao_id>[0-9]+)/$',
        views.adocao_detalhe, name='adocao_detalhe'),
    url(r'^clientes/$', views.clientes, name='clientes'),
    url(r'^clientes/(?P<cliente_id>[0-9]+)/$',
        views.cliente_detalhe, name='cliente_detalhe'),
    url(r'^doadores/$', views.doadores, name='doadores'),
    url(r'^doadores/(?P<doador_id>[0-9]+)/$',
        views.doador_detalhe, name='doador_detalhe'),
    url(r'^animais/$', views.animais, name='animais'),
    url(r'^animais/(?P<animal_id>[0-9]+)/$',
        views.animal_detalhe, name='animal_detalhe'),
    url(r'^racas/$', views.racas, name='racas'),
    url(r'^racas/(?P<raca_id>[0-9]+)/$',
        views.raca_detalhe, name='raca_detalhe'),
    url(r'^busca/$', views.busca, name='busca'),
]
