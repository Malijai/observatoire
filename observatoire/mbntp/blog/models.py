# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import permalink
from django.contrib.auth.models import User

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Tag(models.Model):
   mot_en = models.CharField(max_length=100, unique=True, error_messages={'unique':"Ce mot clef existe déjà"})
   slug = models.SlugField(max_length=100)

   class Meta:
       ordering = ['mot_en']

   def __str__(self):
       return '%s' % self.mot_en

   def __unicode__(self):
       return u'%s' % self.mot_en

   @permalink
   def get_absolute_url(self):
       return ('view_blog_tag', None, {'slug': self.slug})

class Entree(models.Model):
    titre_en = models.CharField(max_length=200)
    texte_en = models.TextField()
    author = models.ForeignKey(User, blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
       ordering = ['-posted']

    def __str__(self):
        return '%s' % self.titre_en

    def __unicode__(self):
        return u'%s' % self.titre_en

class Commentaire(models.Model):
    texte_en = models.TextField()
    entree = models.ForeignKey(Entree, on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return  '%s' % self.texte_en

    def __unicode__(self):
        return u'%s' % self.texte_en

    


