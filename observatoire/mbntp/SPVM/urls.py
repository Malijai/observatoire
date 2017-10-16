from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from .views import listequestions, SelectPersonne

urlpatterns = [
#    url(r'^$', BlogIndex.as_view(), name='blogindex'),
    url(r'^$', SelectPersonne, name='SelectPersonne'),
#    url(r'^questionnaire/(?P<pk>[^\.]+).html', views.listequestions, name='listequestions'),
    url(r'^list.html', views.listequestions, name='listequestions'),
    url(r'^save/(?P<qid>[-\w]+)/(?P<pid>[-\w]+)/$', views.savereponses, name='savereponses'),
#    url(r'^(?P<pk>[-\w]+)/$', views.listequestions, name='listequestions'),
]


