# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Ressource(models.Model):
    nom = models.CharField(max_length=250)
    acronyme = models.CharField(max_length=50, blank=True, null=True)
    depuis = models.CharField(max_length=100, blank=True, null=True)
    descriptif = models.TextField()
    domaine = models.CharField(max_length=250, blank=True, null=True, help_text="Domaines d'intervention / pratiques")
    siteweb = models.CharField(max_length=250, blank=True, null=True)
    courriel = models.CharField(max_length=250, blank=True, null=True)
    telephone = models.CharField(max_length=250, blank=True, null=True)
    motsclef = models.CharField(max_length=250, verbose_name="Mots Clefs", blank=True, null=True, help_text="Champ provisoire, sera remplacé par une liste de choix, séparer les mots par ; ")
    autresinfos = models.CharField(max_length=250, verbose_name="Autres informations", blank=True, null=True)
    author = models.ForeignKey(User, related_name='AssistantRessource',blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    region = models.CharField(max_length=250, blank=True, null=True)
    popcible = models.CharField(max_length=250, verbose_name="Population cible", blank=True, null=True)

    def __str__(self):
        return '{}, {}'.format(self.acronyme.upper(), self.nom)

    def __unicode__(self):
        return u'{}'.format(self.__str__())


class Document(models.Model):
    docfile = models.FileField(upload_to='DocsRessources', verbose_name="Documentation utile", blank=True, null=True)
    description = models.CharField(max_length=100, verbose_name="Brève description", blank=True, null=True, help_text="Nom explicite et court du fichier (par exemple rapport annuel)")
    ressource = models.ForeignKey(Ressource)
    author = models.ForeignKey(User, related_name='AssistantDocument', blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)



