# -*- coding: utf-8 -*-
from django import forms

from .models import Document, Dossier
from django.utils.translation import ugettext_lazy as _

#class DocumentForm(forms.Form):
#    docfile = forms.FileField(
#        label='Select a file',
#        help_text='max. 42 megabytes'
#)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('docfile','comment',)
        labels = {'docfile': _('Selectionner un fichier'),
                  'comment': _('Description'),}
        help_text = {'docfile': ('max. 10 megabytes'), }

class DossierForm(forms.ModelForm):
    class Meta:
        model = Dossier
        fields = ('nomdossier','comment',)
        labels = {'nomdossier': _('Nom du sous-dossier'),
                  'comment': _('Description'),}


