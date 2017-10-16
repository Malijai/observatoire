# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Delits(models.Model):
    #violent; sexuel ...
    description = models.CharField(max_length=100, verbose_name="Types de délits")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Ages(models.Model):
    #mineurs + majeurs; majeurs seulement ...
    description = models.CharField(max_length=100, verbose_name="Classes d'ages")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Diagnostics(models.Model):
    description = models.CharField(max_length=100, verbose_name="Types de diagnostics")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Decisions(models.Model):
    description = models.CharField(max_length=100, verbose_name="Auteurs des décisions")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Prerequis(models.Model):
    description = models.CharField(max_length=100, verbose_name="Prérequis")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Typetraitements(models.Model):
    description = models.CharField(max_length=100, verbose_name="Types de traitements")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Echecs(models.Model):
    description = models.CharField(max_length=100, verbose_name="Conséquences en cas de non suivi du programme")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Succes(models.Model):
    # mineurs + majeurs; majeurs seulement ...
    description = models.CharField(max_length=100, verbose_name="Conséquences en cas d'adhérence au programme")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Surveillances(models.Model):
    # mineurs + majeurs; majeurs seulement ...
    description = models.CharField(max_length=100, verbose_name="Surveillance")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description

class Fins(models.Model):
    # mineurs + majeurs; majeurs seulement ...
    description = models.CharField(max_length=100, verbose_name="Achèvement du programme")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Tribunal(models.Model):
    nom = models.CharField(max_length=250,verbose_name="Nom du tribunal")
    province = models.CharField(max_length=250,verbose_name="Province où se situe ce tribunal")
    adresse = models.CharField(max_length=250,verbose_name="Adresse complète du tribunal")
    tsmfile = models.FileField(upload_to='DocsReferences', verbose_name="Article / Rapport à propos de ce tribunal", blank=True, null=True)
    typedelits = models.ManyToManyField(Delits, verbose_name="Types de délits acceptés")
    age = models.ManyToManyField(Ages, verbose_name="Mineurs ou majeurs")
    diagnostic = models.ManyToManyField(Diagnostics, verbose_name="Type de troubles admis")
    decision = models.ManyToManyField(Decisions, verbose_name="Auteurs de la décision")
    prerequis = models.ManyToManyField(Prerequis, verbose_name="Prérequis")
    traitementtype = models.ManyToManyField(Typetraitements, verbose_name="Traitements proposés")
    traitementduree = models.CharField(max_length=250,verbose_name="Durée du traitement", blank=True, null=True)
    medication = models.BooleanField(verbose_name="Cliquer si la médication est obligatoire")
    echec = models.ManyToManyField(Echecs, verbose_name="Actions en cas de non conformités")
    succes = models.ManyToManyField(Succes, verbose_name="Actions en cas d'adhérence au programme")
    surveillance = models.ManyToManyField(Surveillances, verbose_name="Surveillance du programme")
    issue = models.ManyToManyField(Fins, verbose_name="Achèvement du programme par :")
    evaluation = models.BooleanField(verbose_name="Cliquer si ce tribunal a fait l'objet d'une évaluation de son programme")
    resume = models.TextField(verbose_name="Résumé de l'évaluation", blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s' % self.nom

    def __unicode__(self):
        return u'%s' % self.nom

