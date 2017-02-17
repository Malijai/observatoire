from django.conf.urls import url
from . import views
from .views import test, BlogDetail, listing, EntreesYearArchiveView
from django.contrib.auth.decorators import login_required

urlpatterns = [
#    url(r'^$', BlogIndex.as_view(), name='blogindex'),
    url(r'^$', listing, name='blogindex'),
    url(r'^test/$', test),
    url(r'^(?P<year>[0-9]{4})/$', EntreesYearArchiveView.as_view(), name="article_year_archive"),
    url(r'^(?P<pk>[-\w]+)/$', login_required(BlogDetail.as_view()), name='blogdetail'),
    url(r'^(?P<pk>[-\w]+)/comment/new/$', views.commentaire_new, name='commentaire_new'),
    url(r'^tag/(?P<slug>[^\.]+).html', views.view_tag, name='view_blog_tag'),
    url(r'entree/new/$', views.entree_new, name='entree_new'),
    url(r'tag/new/$', views.tag_new, name='tag_new'),
]
