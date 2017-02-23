# coding=utf-8
from django import forms

from .models import Commentaire, Entree, Tag

class CommentaireForm(forms.ModelForm):
     class Meta:
        model = Commentaire
        fields = ('texte_en', )
        labels = {'texte_en': ('Votre commentaire'), }


class EntreeForm(forms.ModelForm):
     class Meta:
        model = Entree
        fields = ('titre_en', 'texte_en', 'tag')
        labels = {'texte_en': ('Votre texte'),
                  'titre_en': ('Votre titre doit être explicite'),
                  'tag': ('Indiquez des mots clefs (Ctrl + Click)'),}

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('mot_en', )
        labels = {'mot_en': ('Entrer un mot clef'),}


class RechercheForm(forms.Form):
    recherchetexte = forms.CharField(label='Texte à chercher', max_length=100)
