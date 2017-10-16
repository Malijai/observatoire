from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Typequestion(models.Model):
    nom = models.CharField(max_length=200, )
    table = models.CharField(max_length=200, blank=True, null=True)
    taille = models.CharField(max_length=200, )

    def __str__(self):
        return '%s' % self.nom

    def __unicode__(self):
        return u'%s' % self.nom


class Questionnaire(models.Model):
    nom_en = models.CharField(max_length=200,)
    nom_fr = models.CharField(max_length=200,)
    description = models.CharField(max_length=200,)

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

DEFAULT_PARENT_ID = 1
class Question(models.Model):
    questionno = models.IntegerField()
    questionen = models.CharField(max_length=255,)
    questionnaire = models.ForeignKey(Questionnaire)
    typequestion = models.ForeignKey(Typequestion)
    parent= models.ForeignKey("self", default=DEFAULT_PARENT_ID)
    relation = models.CharField(blank=True, null=True, max_length=45,)
    cible = models.CharField(blank=True, null=True, max_length=45,)
    varname = models.CharField(blank=True, null=True, max_length=45,)
    aidefr = models.TextField(blank=True, null=True)
    aideen = models.TextField(blank=True, null=True)
    qstyle = models.CharField(blank=True, null=True, max_length=45,)

    class Meta:
        ordering = ['questionno']

    def __str__(self):
        return '%s' % self.questionen

    def __unicode__(self):
        return u'%s' % self.questionen


class Condition(models.Model):
    parent = models.ForeignKey(Question, related_name='QuestionParent')
    enfant = models.ForeignKey(Question, related_name='QuestionEnfant')
    relation = models.CharField(blank=True, null=True, max_length=200,)
    cible = models.CharField(blank=True, null=True, max_length=200,)
    questionnaire = models.ForeignKey(Questionnaire)

    def __str__(self):
        return '%s' % self.parent

    def __unicode__(self):
        return u'%s' % self.parent


class Province(models.Model):
    nom_en = models.CharField(max_length=200,)
    nom_fr = models.CharField(max_length=200,)

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en


class Pays(models.Model):
    nom_en = models.CharField(max_length=200,)
    nom_fr = models.CharField(max_length=200,)

    class Meta:
       ordering = ['nom_en']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

class Personne(models.Model):
    code = models.CharField(max_length=200,)
    province = models.ForeignKey(Province)
    ddn = models.CharField(max_length=200,blank=True, null=True)
    diedon = models.CharField(max_length=200,blank=True, null=True)
    dod = models.CharField(max_length=200,blank=True, null=True)
    completed = models.CharField(max_length=200,blank=True, null=True)
    sexe = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assistant = models.ForeignKey(User)


DEFAULT_PID = 1
class Resultat(models.Model):
    personne = models.ForeignKey(Personne)
    question = models.ForeignKey(Question)
    assistant = models.ForeignKey(User)
#    verdict_id
#    audience_id
    province = models.ForeignKey(Province,default=DEFAULT_PID)
    reponsetexte = models.CharField(max_length=200,blank=True, null=True)
    reponsecode = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('personne', 'question','assistant'),)

class Reponse(models.Model):
    question = models.ForeignKey(Question)
    reponse_no = models.CharField(max_length=200)
    reponse_valeur = models.CharField(max_length=200)
    reponse_en = models.CharField(max_length=200,)
    reponse_fr = models.CharField(max_length=200,)
    questionnaire = models.ForeignKey(Questionnaire)

    class Meta:
       ordering = ['reponse_valeur']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en


class Langue(models.Model):
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )

    class Meta:
        ordering = ['nom_en']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en


class Violation(models.Model):
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )

    class Meta:
        ordering = ['nom_en']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

class Hcr(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )

    class Meta:
        ordering = ['reponse_valeur']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

class Victime(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )

    class Meta:
        ordering = ['reponse_valeur']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

class Posologie(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )

    class Meta:
        ordering = ['reponse_valeur']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

class Etablissement(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )

    class Meta:
        ordering = ['reponse_valeur']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en

class Municipalite(models.Model):
    reponse_valeur = models.CharField(max_length=200)
    nom_en = models.CharField(max_length=200, )
    nom_fr = models.CharField(max_length=200, )
    province = models.ForeignKey(Province, default=DEFAULT_PID)

    class Meta:
        ordering = ['reponse_valeur']

    def __str__(self):
        return '%s' % self.nom_en

    def __unicode__(self):
        return u'%s' % self.nom_en
