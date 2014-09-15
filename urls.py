from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sistema.views import sistema, login, menu
from contatos.views import contatos_listar, contatos_cadastrar, contatos_editar, contatos_excluir

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^contatos/$', contatos_listar),
    url(r'^contatos/listar/$', contatos_listar),
    url(r'^contatos/cadastrar/$', contatos_cadastrar),
    url(r'^contatos/editar/(?P<contato_id>\d+)/$', contatos_editar),
    url(r'^contatos/excluir/(?P<contato_id>\d+)/$', contatos_excluir),
    url(r'^', menu),
    url(r'^/login/$', login),
)

# urlpatterns += patterns(
#     (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
# )

urlpatterns += staticfiles_urlpatterns()