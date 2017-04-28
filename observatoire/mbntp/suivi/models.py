# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=200, blank=True, null=True)
    affiliation = models.CharField(max_length=200, blank=True, null=True)
    courriel = models.CharField(max_length=200, blank=True, null=True)
    domaine = models.CharField(max_length=250, blank=True, null=True)
    responsable = models.ForeignKey(User, blank=True)
    envoifait = models.DateField(blank=True, null=True)
    reponse = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.nom.upper(), self. prenom)

    def __unicode__(self):
        return u'{}'.format(self.__str__())