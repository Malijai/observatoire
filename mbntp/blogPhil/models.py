from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Entree(models.Model):
    titre_en = models.CharField(max_length=200)
    texte_en = models.TextField()
    #author = models.ForeignKey(User, blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return  '%s' % self.titre_en

    def __unicode__(self):
        return u'%s' % self.titre_en


@python_2_unicode_compatible
class Commentaire(models.Model):
    texte_en = models.TextField()
    entree = models.ForeignKey(Entree, on_delete=models.CASCADE)
    #author = models.ForeignKey(User, blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return  '%s' % self.texte_en

    def __unicode__(self):
        return u'%s' % self.texte_en

    


