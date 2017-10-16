# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Delits, Ages, Diagnostics, Decisions, Prerequis, Typetraitements, Echecs, Succes, Surveillances, Fins, Tribunal


class TribunalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': [('nom', 'province'), 'adresse', 'tsmfile']}),
        ('Eligibilité', {'fields': ['typedelits', 'age','diagnostic']}),
        ('Processus d admission', {'fields': [('decision', 'prerequis')]}),
        ('Caractéristiques du traitement', {'fields': ['traitementtype', 'traitementduree','medication']}),
        ('Conformité & Adhérence', {'fields': ['echec', 'succes', 'surveillance', 'issue']}),
        ('Évaluation', {'fields': ['evaluation', 'resume']}),
    ]

    list_display = ('nom', 'province')

    list_filter = ['province','evaluation']


def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Tribunal, TribunalAdmin)
admin.site.register(Delits)
admin.site.register(Ages)
admin.site.register(Diagnostics)
admin.site.register(Decisions)
admin.site.register(Prerequis)
admin.site.register(Typetraitements)
admin.site.register(Echecs)
admin.site.register(Succes)
admin.site.register(Surveillances)
admin.site.register(Fins)

