# coding=utf-8
from django import forms

from .models import Commentaire, Entree

class CommentaireForm(forms.ModelForm):
     class Meta:
        model = Commentaire
        fields = ('texte_en', )
        labels = {'texte_en': ('Votre commentaire'), }


class EntreeForm(forms.ModelForm):
     class Meta:
        model = Entree
        fields = ('titre_en', 'texte_en')
        labels = {'texte_en': ('Votre texte'),
                  'titre_en': ('Votre titre doit être explicite')}