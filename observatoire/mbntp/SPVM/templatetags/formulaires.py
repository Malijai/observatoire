from __future__ import unicode_literals
from django import template
from django.http import QueryDict
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
import re
from django.apps import apps
from SPVM.models import Typequestion, Resultat, Reponse
from django import forms

register = template.Library()


@register.simple_tag
def fait_dichou(a,b, *args, **kwargs):
    qid = a
    type = b
    personneid = kwargs['pid']
    relation = kwargs['relation']
    cible = kwargs['cible']

    existe = Resultat.objects.filter(personne__id=personneid, question__id=qid, assistant__id=1).count()
    if existe > 0:
        ancienne = Resultat.objects.get(personne__id=personneid, question__id=qid, assistant__id=1)
        defaultvalue = ancienne.reponsetexte
    else:
        defaultvalue = ''

    IDCondition = ''
    if relation != '' and cible != '':
        IDCondition = 'row-' + str(qid) + 'X' +  str(relation) + 'X' +  str(cible)
    else:
        IDCondition = "q" + str(qid)
    if type == "DICHO":
        liste = [(1, 'Yes'),(0, 'No')]
    else:
        liste = [(1, 'Yes'),(0, 'No'),(98, 'NA'), (99,'Unknown')]
    name = "q" + str(qid)
    question = forms.RadioSelect(choices = liste, attrs={'id': IDCondition,'name': name, })

    return enlevelisttag(question.render(name, defaultvalue))


@register.simple_tag
def fait_date(a,b, *args, **kwargs):
    qid = a
    personneid = kwargs['pid']
    relation = kwargs['relation']
    cible = kwargs['cible']

    existe = Resultat.objects.filter(personne__id=personneid, question__id=qid, assistant__id=1).count()
    if existe > 0:
        ancienne = Resultat.objects.get(personne__id=personneid, question__id=qid, assistant__id=1)
        defaultvalue = ancienne.reponsetexte
    else:
        defaultvalue = ''

    IDCondition = ''
    if relation != '' and cible != '':
        IDCondition = 'row-' + str(qid) + 'X' +  str(relation) + 'X' +  str(cible)
    else:
        IDCondition = "q" + str(qid)
    name = "q" + str(qid)
    question = forms.DateInput(format=('%d-%m-%Y'), attrs={'id': IDCondition,'name': name,})

    return question.render(name, defaultvalue)


@register.simple_tag
def fait_textechar(a,b, *args, **kwargs):
    qid = a
    type = b
    personneid = kwargs['pid']
    relation = kwargs['relation']
    cible = kwargs['cible']

    existe = Resultat.objects.filter(personne__id=personneid, question__id=qid, assistant__id=1).count()
    if existe > 0:
        ancienne = Resultat.objects.get(personne__id=personneid, question__id=qid, assistant__id=1)
        defaultvalue = ancienne.reponsetexte
    else:
        defaultvalue = ''

    IDCondition = ''
    if relation != '' and cible != '':
        IDCondition = "row-" + str(qid) + "X" +  str(relation) + "X" +  str(cible)
    else:
        IDCondition = "q" + str(qid)

    name = "q" + str(qid)

    if type == 'STRING':
        question = forms.TextInput(attrs={'size': 10, 'id': IDCondition,'name': name,})
    else:
        question = forms.NumberInput(attrs={'size': 10, 'id': IDCondition,'name': name,})

    return question.render(name, defaultvalue)


@register.simple_tag
def fait_table(a,b, *args, **kwargs):
    #questid type
    qid = a
    personneid = kwargs['pid']
    relation = kwargs['relation']
    cible = kwargs['cible']
    typetable = {"PROVINCE": "province", "PAYS": "pays", "LANGUE": "langue","VIOLATION": "violation"}
    tableext = typetable[b]

    existe = Resultat.objects.filter(personne__id=personneid, question__id=qid, assistant__id=1).count()
    if existe > 0:
        ancienne = Resultat.objects.get(personne__id=personneid, question__id=qid, assistant__id=1)
        defaultvalue = ancienne.reponsetexte
    else:
        defaultvalue = ''

    IDCondition = ''
    if relation != '' and cible != '':
        IDCondition = "row-" + str(qid) + "X" +  str(relation) + "X" +  str(cible)
    else:
        IDCondition = "q" + str(qid)

    Klass = apps.get_model('SPVM', tableext)
    # Klass = apps.get_model('SPVM', typetable[b])
    listevaleurs = Klass.objects.all()
    name = "q" + str(qid)
    liste = [('','')]
    for valeur in listevaleurs:
       vid=str(valeur.id)
       nen=valeur.nom_en
       liste.append((vid, nen))

    question = forms.Select(choices = liste, attrs={'id': IDCondition,'name': name, })

    return question.render(name, defaultvalue)

@register.simple_tag
def fait_reponse(a,b, *args, **kwargs):
    #Pour listes de valeurs specifiques a chaque question
    #questid type
    qid = a
    personneid = kwargs['pid']
    relation = kwargs['relation']
    cible = kwargs['cible']

    existe = Resultat.objects.filter(personne__id=personneid, question__id=qid, assistant__id=1).count()
    if existe > 0:
        ancienne = Resultat.objects.get(personne__id=personneid, question__id=qid, assistant__id=1)
        defaultvalue = ancienne.reponsetexte
    else:
        defaultvalue = ''

    IDCondition = ''
    if relation != '' and cible != '':
        IDCondition = "row-" + str(qid) + "X" +  str(relation) + "X" +  str(cible)
    else:
        IDCondition = "q" + str(qid)

    listevaleurs = Reponse.objects.filter(question__id=qid, )
    nombrelistevaleurs = Reponse.objects.filter(question__id=qid).count()
    name = "q" + str(qid)
    liste = []
    for valeur in listevaleurs:
        vid = valeur.reponse_valeur
        nen = valeur.reponse_en
        liste.append((vid, nen))
    if nombrelistevaleurs < 4:
        question = forms.RadioSelect(choices=liste, attrs={'id': IDCondition, 'name': name, })
    else:
        liste.append(('',''))
        question = forms.Select(choices = liste, attrs={'id': IDCondition,'name': name, })

    return enlevelisttag(question.render(name, defaultvalue))


@register.filter
def enlevelisttag(texte):
    ## pour mettre les radiobutton sur une seule ligne
    texte = re.sub(r"(<ul[^>]*>)",r"", texte)
    texte = re.sub(r"(<li[^>]*>)",r"", texte)
    texte = re.sub(r"(</li>)",r"", texte)
    return re.sub(r"(</ul>)",r" ", texte)


@register.simple_tag
def fait_table_valeurs(a,b, *args, **kwargs):
    #pour les tables dont la valeur a enregistrer n'est pas l'id mais la reponse_valeur
    qid = a
    personneid = kwargs['pid']
    relation = kwargs['relation']
    cible = kwargs['cible']
    typetable = {"HCR20": "hcr","ETABLISSEMENT": "etablissement","MUNICIPALITE": "municipalite", "POSOLOGIE":"posologie", "VICTIME":"victime",}
    tableext = typetable[b]

    existe = Resultat.objects.filter(personne__id=personneid, question__id=qid, assistant__id=1).count()
    if existe > 0:
        ancienne = Resultat.objects.get(personne__id=personneid, question__id=qid, assistant__id=1)
        defaultvalue = ancienne.reponsetexte
    else:
        defaultvalue = ''

    IDCondition = ''
    if relation != '' and cible != '':
        IDCondition = "row-" + str(qid) + "X" +  str(relation) + "X" +  str(cible)
    else:
        IDCondition = "q" + str(qid)

    Klass = apps.get_model('SPVM', tableext)
    # Klass = apps.get_model('SPVM', typetable[b])
    listevaleurs = Klass.objects.all()
    name = "q" + str(qid)
    liste = [('','')]
    for valeur in listevaleurs:
       vid=str(valeur.reponse_valeur)
       nen=valeur.nom_en
       liste.append((vid, nen))

    question = forms.Select(choices = liste, attrs={'id': IDCondition,'name': name, })

    return question.render(name, defaultvalue)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)