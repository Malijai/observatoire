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


class Devis(models.Model):
    # longitudinal, observationnle, retrospective ...
    description = models.CharField(max_length=100, verbose_name="Devis de l'étude")

    class Meta:
        ordering = ['description']

    def __str__(self):
        return '%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description


class Article(models.Model):
    nom = models.CharField(max_length=250,verbose_name="Auteurs", help_text="Nom, Initiale, Chaque nom est séparé par un point virgule")
    annee = models.CharField(max_length=4,verbose_name="Année publication")
    titre  = models.CharField(max_length=250,verbose_name="Référence complète")
    resume = models.TextField(verbose_name="Objectifs")
    resumecourt = models.CharField(max_length=250,verbose_name="Résumé en Français vulgarisé", help_text="255 caractères au max, pour affichage futur sur le site")
    articlefile = models.FileField(upload_to='DocsReferences', verbose_name="Fichier de l'article analysé", blank=True, null=True)
    originebd = models.ManyToManyField(Originebd, verbose_name="BD où l'article a été trouvé")
    typepub = models.ManyToManyField(Typepub,verbose_name="Type de publication")
    interception = models.ManyToManyField(Interception, verbose_name="Niveau d'interception")
    interceptiontxt = models.TextField(verbose_name="Détails niveau d'interceptions",blank=True, null=True)
    region = models.CharField(verbose_name="Lieu (Pays, ville etc)", max_length=250, blank=True, null=True, help_text="Province du QC, Canada, Autre pays (préciser) ... ")
    typeparticipanttxt = models.TextField(verbose_name="Description sommaire de la population à l'étude", blank=True, null=True)
    comparaisonouinon = models.BooleanField(verbose_name="Cliquer s'il y a un groupe de comparaison")
    comparaisontxt = models.TextField(verbose_name="Description sommaire du groupe de comparaison", blank=True, null=True)
    nparticipants= models.TextField(verbose_name="N des différents groupes", blank=True, null=True)
    hommesfemmes = models.TextField(verbose_name="Proportion des hommes et femmes (% hommes)", blank=True, null=True)
    agemoyen= models.TextField(verbose_name="Moyennes d'age des différents groupes", blank=True, null=True)
    typeparticipant = models.ManyToManyField(Typeparticipant, verbose_name="Type de participants à l'étude")
    typeetude = models.ManyToManyField(Typeetude, verbose_name="Type d'étude, méthode")
    devisetude = models.ManyToManyField(Devis,verbose_name="Devis de l'étude")
    typeetudetxt = models.TextField(verbose_name="Détails type étude", blank=True, null=True)
    duree = models.TextField(verbose_name="Durée du suivi pour l'étude (ou étendue temporelle)", blank=True, null=True)
    mesuresresultats = models.TextField(verbose_name="Outcomes mesurés pour cette étude",blank=True, null=True, help_text="Arrestation, traitement / référence, récidive, incarcération ... ")
    tauxmesures = models.TextField(verbose_name="Taux de succès / échecs", blank=True, null=True)
    analyses = models.TextField(verbose_name="Principaux résultats (ceux du résumé + conclusion/discussion", blank=True, null=True, help_text="Ne pas oublier les résultats négatifs; Quali : thèmes ")
    nomprogramme = models.CharField(max_length=250, verbose_name="Nom du programme", blank=True, null=True)
    tsmreference = models.TextField(verbose_name="Référence de la description du PROGRAMME", blank=True, null=True)
    interventiontxt = models.TextField(verbose_name="Services offerts par le programme",blank=True, null=True)
    clientprogramme = models.TextField(verbose_name="Clientèle cible / critères d'admissibilité au programme", blank=True, null=True)
    intervenantprogramme = models.TextField(verbose_name="Professionnels du programme", blank=True, null=True)
    dureeprogramme = models.CharField(max_length=250, verbose_name="Durée du programme (durée du suivi dans le programme)", blank=True, null=True)
    conditionprogramme = models.TextField(verbose_name="Conditions a respecter dans le programme", blank=True, null=True)
    echec = models.CharField(max_length=250, verbose_name="Conséquences en cas de non conformité aux conditions du programme", blank=True, null=True)
    succes = models.CharField(max_length=250, verbose_name="Conséquences en cas d'adhérence au programme", blank=True, null=True)
    origine = models.TextField(verbose_name="Ancien champ ne pas remplir ", blank=True, null=True,
                               help_text="En lien avec une ressource ou un programme? Si oui expliquer")
    autresinfos = models.TextField(verbose_name="Autres informations, commentaires", blank=True, null=True)
    author = models.ForeignKey(User, related_name='AssistantScoping',blank=True, null=True, verbose_name="Assistant ayant procede à l'analyse",)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.annee, self.nom.upper())

    def __unicode__(self):
        return u'{}'.format(self.__str__())
