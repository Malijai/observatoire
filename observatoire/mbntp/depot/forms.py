# -*- coding: utf-8 -*-
from django import forms

from .models import Document, Dossier

#class DocumentForm(forms.Form):
#    docfile = forms.FileField(
#        label='Select a file',
#        help_text='max. 42 megabytes'
#)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('docfile',)
        labels = {'docfile': ('Sélectionner un fichier'),}
#        fields = ('docfile','dossier')
#        labels = {'docfile': ('Select a file'), 'dossier': ('choisir un dossier'),}
        help_text = {'docfile': ('max. 42 megabytes'), }

class DossierForm(forms.ModelForm):
    class Meta:
        model = Dossier
        fields = ('nomdossier',)
        labels = {'nomdossier': ('Taper le nom du sous-dossier'), }


