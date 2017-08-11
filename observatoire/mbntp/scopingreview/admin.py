# -*- coding: utf-8 -*-

from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import Article,Typepub,Typeetude,Typeparticipant,Interception,Originebd,Devis
from django.db import models

class ArticleAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    fieldsets = [
        ('Article', {'fields': [('nom', 'annee'), 'titre', 'resumecourt','articlefile',('originebd','typepub')]}),
        ('Description de l étude', {'fields': [('interception','interceptiontxt'), 'resume',('typeetude','typeetudetxt'),('devisetude', 'duree', 'region')]}),
        ('Population', {'fields': [('typeparticipanttxt','comparaisonouinon', 'comparaisontxt'),('nparticipants','agemoyen','typeparticipant')]}),
        ('Résultats', {'fields': ['mesuresresultats', 'tauxmesures', 'analyses']}),
        ('Intervention / Programme', {'fields': [('nomprogramme','tsmreference'), 'interventiontxt','clientprogramme','intervenantprogramme','dureeprogramme', 'conditionprogramme',('echec', 'succes'),'descriptionprogramme']}),
        ('Autres informations', {'fields': ['autresinfos', 'origine']}),
    ]

    list_display = ('nom', 'annee', 'titre')

    list_filter = ['interception',]


def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Article, ArticleAdmin)
admin.site.register(Typepub)
admin.site.register(Typeetude)
admin.site.register(Typeparticipant)
admin.site.register(Interception)
admin.site.register(Originebd)
admin.site.register(Devis)
