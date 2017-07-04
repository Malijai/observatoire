# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Typepub(models.Model):
    #Empirique, Implémentation, commentaire, revue, éditorial
    description = models.CharField(max_length=100, verbose_name="Type d'étude / publication")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Typeetude(models.Model):
    #Méthode quanti (logitudinale, controlée, randomisée), quasi observationnelle (cohorte, case control)
    # transversale, quali (descriptive, phénoménologique), méthode mixte, implantation
    description = models.CharField(max_length=100, verbose_name="Type d'étude, méthode")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description

class Typeparticipant(models.Model):
    #hommes, femmes, adultes, jeunes, tous, diagnostics spécifiques, antécédents spécifiques, non défini
    # professionnels
    description = models.CharField(max_length=100, verbose_name="Type de participants")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Interception(models.Model):
    #1 Law Enforcement/Emergency Services, 2 Post-Arrest Initial Detention/Initial Hearings; 3 Post-Initial Hearings: Jail/Prison, Courts, Forensic Evaluations & Forensic;
    # 4 Re-Entry From Jails, State Prisons, & Forensic Hospitalization #5 Community Corrections & Community Support
    description = models.CharField(max_length=100, verbose_name="Niveau d'interception")

    class Meta:
       ordering = ['description']

    def __str__(self):
       return '%s' % self.description

    def __unicode__(self):
       return u'%s' % self.description


class Originebd(models.Model):
    #PubMed, PsychInfo, Embase, BD droit, NCJRS, Web of Science, CAIRN, ÉRUDIT
    description = models.CharField(max_length=100, verbose_name="BD où l'article a été trouvé")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description

class Article(models.Model):
    nom = models.CharField(max_length=250,verbose_name="Auteurs", help_text="Nom, Initiale, Chaque nom est séparé par un point virgule")
    annee = models.CharField(max_length=4,verbose_name="Année publication")
    titre  = models.CharField(max_length=250)
    resume = models.TextField()
    resumecourt = models.CharField(max_length=250,verbose_name="Résumé en Français vulgarisé", help_text="255 caractères au max, pour affichage futur sur le site")
    articlefile = models.FileField(upload_to='DocsReferences', verbose_name="Article analysé")
    origine = models.TextField(verbose_name="Evaluation programme / ressource listée?", blank=True, null=True, help_text="En lien avec une ressource ou un programme? Si oui expliquer")
    originebd = models.ManyToManyField(Originebd, verbose_name="BD où l'article a été trouvé")
    typepub = models.ManyToManyField(Typepub,verbose_name="Type d'étude / publication")
    typeetude = models.ManyToManyField(Typeetude, verbose_name="Type d'étude, méthode")
    typeetudetxt = models.TextField(verbose_name="Détails type étude", blank=True, null=True)
    typeparticipant = models.ManyToManyField(Typeparticipant, verbose_name="Type de participants")
    typeparticipanttxt = models.TextField(verbose_name="Détails participants", blank=True, null=True)
    comparaisontxt = models.TextField(verbose_name="Description du groupe de comparaison", blank=True, null=True)
    interception = models.ManyToManyField(Interception, verbose_name="Niveau d'interception")
    interceptiontxt = models.TextField(verbose_name="Détails niveau d'interceptions",blank=True, null=True)
    interventiontxt = models.TextField(verbose_name="Description du programme",blank=True, null=True)
    mesuresresultats = models.TextField(verbose_name="Résultat mesurés par",blank=True, null=True, help_text="Arrestation, traitement / référence, récidive, incarcération ... ")
    analyses = models.TextField(verbose_name="Résultats des analyses", blank=True, null=True, help_text="Descriptives : détails; Quali : thèmes ")
    region = models.CharField(verbose_name="Étendue géographique", max_length=250, blank=True, null=True, help_text="Province du QC, Canada, Autre pays (préciser) ... ")
    autresinfos = models.TextField(verbose_name="Autres informations", blank=True, null=True)
    author = models.ForeignKey(User, related_name='AssistantScoping',blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.annee, self.nom.upper())

    def __unicode__(self):
        return u'{}'.format(self.__str__())




