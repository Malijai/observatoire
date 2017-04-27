# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=200, blank=True)
    affiliation = models.CharField(max_length=200, blank=True)
    courriel = models.CharField(max_length=200, blank=True)
    domaine = models.CharField(max_length=250, blank=True)
    responsable = models.ForeignKey(User, blank=True)
    envoifait = models.DateField(blank=True)
    reponse = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return '{}, {}'.format(self.nom.upper(), self. prenom)

    def __unicode__(self):
        return u'{}'.format(self.__str__())