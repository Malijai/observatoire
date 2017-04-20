from __future__ import unicode_literals

from django.db import models


class Dossier(models.Model):
    nomdossier = models.CharField(max_length=100)
    comment = models.CharField(max_length=200, blank=True, null=True)
    parentId = models.ForeignKey("self")

    def __str__(self):
        return '%s' % self.nomdossier

    def __unicode__(self):
        return u'%s' % self.nomdossier

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')
#    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    comment = models.CharField(max_length=200, blank=True, null=True)
    dossier = models.ForeignKey(Dossier)
    # nicename = models.CharField(max_length=100, blank=True, null=True)