from django.conf.urls import url

from . import views
from .views import accueil

urlpatterns = [
    url(r'^$', accueil, name='accueil'),
]
