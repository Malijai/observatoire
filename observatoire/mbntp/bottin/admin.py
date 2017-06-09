# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Ressource, Document


#class DocumentInline(admin.StackedInline):
class DocumentInline(admin.TabularInline):
    model = Document

    fields = ['docfile','description']


class RessourceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': ['nom', 'acronyme', 'siteweb','courriel','telephone']}),
        ('Description', {'fields': ['depuis', 'descriptif','domaine','popcible','autresinfos']}),
        ('Mots clefs (les séparer par un point virgule ; )', {'fields': ['motsclef', 'region']}),
    ]

    inlines = [DocumentInline,]

    list_display = ('acronyme', 'nom', 'domaine')

    list_filter = ['domaine',]

def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Ressource, RessourceAdmin)