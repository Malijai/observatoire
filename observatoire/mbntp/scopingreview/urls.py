from django.conf.urls import url

from . import views
from .views import fait_csv, some_pdf, PdfExtraction

urlpatterns = [
    url(r'^csv/$', fait_csv, name='fait_csv'),
    url(r'^pdf/(?P<pk>[-\w]+)/$', some_pdf, name='some_pdf'),
    url(r'^$', PdfExtraction, name='listearticles'),
]

