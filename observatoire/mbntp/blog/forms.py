# coding=utf-8
from django import forms

from .models import Commentaire, Entree, Tag
from django.utils.translation import ugettext as _

class CommentaireForm(forms.ModelForm):
     class Meta:
        model = Commentaire
        fields = ('texte_en', )
        labels = {'texte_en': ('Votre commentaire'), }


class EntreeForm(forms.ModelForm):
     class Meta:
        model = Entree
        fields = ('titre_en', 'texte_en', 'tag')
        labels = {'texte_en': _('Votre texte'),
                  'titre_en': _('Votre titre doit etre explicite'),
                  'tag': _('Indiquez des mots clefs (Ctrl + Click)'),}

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('mot_en', )
        labels = {'mot_en': _('Entrer un mot clef'),}


class RechercheForm(forms.Form):
    recherchetexte = forms.CharField(label='Texte à chercher', max_length=100)

