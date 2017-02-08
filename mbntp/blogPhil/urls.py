from django.conf.urls import url
from . import views
from .views import test, BlogIndex, BlogDetail, listing

urlpatterns = [
#    url(r'^$', BlogIndex.as_view(), name='blogindex'),
    url(r'^$', listing, name='blogindex'),
    url(r'^test/$', test),
#    url(r'^list/$', listing),
    url(r'^(?P<pk>[-\w]+)/$', BlogDetail.as_view(), name='blogdetail'),
    url(r'^(?P<pk>[-\w]+)/comment/new/$', views.commentaire_new, name='commentaire_new'),
    url(r'entree/new/$', views.entree_new, name='entree_new'),
]
