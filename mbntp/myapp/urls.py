from django.conf.urls import url

from .views import dossier_new, pardossier

urlpatterns = [
#    url(r'^doclist/$', doclist, name='doclist'),
    url(r'^dossierslist/$', dossier_new, name='dossierslist'),
    url(r'^dossiers/(?P<pid>[-\w]+)/$', pardossier , name='dossier'),
]

