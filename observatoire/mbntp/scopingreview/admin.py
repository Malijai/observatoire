# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import Article,Typepub,Typeetude,Typeparticipant,Interception,Originebd,Devis
from django.db import models
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    fieldsets = [
        ('Article', {'fields': [('nom', 'annee'), 'titre', 'resumecourt','articlefile',('originebd','typepub')]}),
        ('Description de l étude', {'fields': [('interception','interceptiontxt'), 'resume',('typeetude','typeetudetxt'),('devisetude', 'duree', 'region')]}),
        ('Population', {'fields': [('typeparticipanttxt','typeparticipant'),('comparaisonouinon', 'comparaisontxt'),('nparticipants','agemoyen','hommesfemmes')]}),
        ('Résultats', {'fields': ['mesuresresultats', 'tauxmesures', 'analyses']}),
        ('Intervention / Programme', {'fields': [('nomprogramme','tsmreference'), 'interventiontxt','clientprogramme','intervenantprogramme','dureeprogramme', 'conditionprogramme',('echec', 'succes')]}),
        ('Autres informations', {'fields': ['autresinfos', 'origine',]}),
    ]

    list_display = ('nom', 'annee', 'titre', 'author')

    list_filter = ['interception', 'author',]


    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Typepub)
#admin.site.register(Typeetude)  #a enlever
admin.site.register(Typeparticipant)
#admin.site.register(Interception)  #a enlever
#admin.site.register(Originebd)  #a enlever
admin.site.register(Devis)


