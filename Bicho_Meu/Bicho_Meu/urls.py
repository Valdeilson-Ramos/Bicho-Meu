from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'Bicho_Meu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', TemplateView.as_view(template_name='index.html'),
    name='index'),
    url(r'^adocao/',
        include('adocao.urls', namespace='adocao')),
    url(r'^admin/', include(admin.site.urls)),
]
