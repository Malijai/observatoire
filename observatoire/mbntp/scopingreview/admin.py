# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Article,Typepub,Typeetude,Typeparticipant,Interception,Originebd


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Article', {'fields': [('nom', 'annee'), 'titre', 'resume','articlefile',('originebd','origine')]}),
        ('Description', {'fields': ['typepub', ('typeetude','typeetudetxt'),('interception','interceptiontxt')]}),
        ('Population', {'fields': [('typeparticipant', 'typeparticipanttxt'),'comparaisontxt','region']}),
        ('Intervention / Programme', {'fields': ['interventiontxt']}),
        ('Résultats', {'fields': ['mesuresresultats', 'analyses']}),
        ('Autres informations', {'fields': ['autresinfos']}),
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
