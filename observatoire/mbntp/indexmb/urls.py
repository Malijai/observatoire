from django.conf.urls import url

from . import views
from .views import indexMB

urlpatterns = [
    #url(r'^debut/$', indexMB, name='indexMB'),
    url(r'^', indexMB, name='indexMB'),
]
