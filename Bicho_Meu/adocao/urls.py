from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.AdocaoDetalhe.as_view(), name='adocao_detalhe'),
    url(r'^clientes/$', views.ClientesView.as_view(), name='clientes'),
    url(r'^clientes/(?P<pk>[0-9]+)/$',
        views.ClienteDetalhe.as_view(), name='cliente_detalhe'),
    url(r'^doadores/$', views.DoadoresView.as_view(), name='doadores'),
    url(r'^doadores/(?P<pk>[0-9]+)/$',
        views.DoadorDetalhe.as_view(), name='doador_detalhe'),
    url(r'^animais/$', views.AnimaisView.as_view(), name='animais'),
    url(r'^animais/(?P<pk>[0-9]+)/$',
        views.AnimalDetalhe.as_view(), name='animal_detalhe'),
    url(r'^racas/$', views.RacasView.as_view(), name='racas'),
    url(r'^racas/(?P<pk>[0-9]+)/$',
        views.RacaDetalhe.as_view(), name='raca_detalhe'),
    url(r'^busca/$', views.busca, name='busca'),
]

'''
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
'''
