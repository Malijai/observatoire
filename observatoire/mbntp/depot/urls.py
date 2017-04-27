from django.conf.urls import url

from . import views
from .views import dossier_new, pardossier

urlpatterns = [
#    url(r'^doclist/$', doclist, name='doclist'),
    url(r'^dossierslist/$', dossier_new, name='dossierslist'),
    url(r'^dossiers/(?P<pid>[-\w]+)/$', pardossier , name='dossier'),
    url(r'^(?P<pid>[-\w]+)/dossier/new/$', views.dossier_new, name='dossier_new'),
]

