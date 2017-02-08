from django.conf.urls import url

from .views import doclist, dossier_new

urlpatterns = [
    url(r'^doclist/$', doclist, name='doclist'),
    url(r'^dossierslist/$', dossier_new, name='dossierslist')
]

