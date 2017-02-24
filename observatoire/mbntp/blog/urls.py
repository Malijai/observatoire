from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from .views import index, BlogDetail, listing, get_recherchetexte

urlpatterns = [
#    url(r'^$', BlogIndex.as_view(), name='blogindex'),
    url(r'^$', listing, name='blogindex'),
    url(r'^index/$', index),
    url(r'^recherche/$', get_recherchetexte, name='recherche'),
    url(r'^(?P<pk>[-\w]+)/$', login_required(BlogDetail.as_view()), name='blogdetail'),
    url(r'^(?P<pk>[-\w]+)/comment/new/$', views.commentaire_new, name='commentaire_new'),
    url(r'^tag/(?P<slug>[^\.]+).html', views.view_tag, name='view_blog_tag'),
    url(r'entree/new/$', views.entree_new, name='entree_new'),
    url(r'tag/new/$', views.tag_new, name='tag_new'),

]
