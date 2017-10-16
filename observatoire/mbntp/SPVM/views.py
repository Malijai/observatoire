# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, cookie
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Typequestion, Questionnaire,Question,Condition,Resultat,Personne
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url=settings.LOGIN_URI)
def listequestions(request):
    #affiche toutes les questions
    question_list = Question.objects.all()
    enfant_list = Question.objects.filter(parent__gt = 1)

    enfants = []
    for enfant in Question.objects.filter(parent__gt = 1):
        enfants.append(enfant.parent_id)

    parent_list=Question.objects.filter(pk__in=enfants)

    riens = Question.objects.filter(parent = 1)

    orphelins = [x for x in riens if x not in enfants and x not in parent_list]

    return render(request, 'spvm/list.html',
                  {'orphelins' : orphelins,
                   'questions': question_list,
                   'enfants': enfant_list,
                   'parents': parent_list,})


@login_required(login_url=settings.LOGIN_URI)
def savereponsesold(request,qid,pid):
    #affiche le formulaire pour 1 questionnaire et 1 personne
    personneid = pid
    questionnaireid = qid

    personne = Personne.objects.get(pk=personneid)
    question_list = Question.objects.filter(questionnaire=questionnaireid)
    enfant_list = Question.objects.filter(parent__gt = 1, questionnaire=questionnaireid)
    enfants = Question.objects.filter(question__parent__gt=1, questionnaire=questionnaireid)
    # enfants = []
    # for enfant in Question.objects.filter(parent__gt=1, questionnaire=questionnaireid):
    #     enfants.append(enfant.parent_id)

    parent_list = Question.objects.filter(pk__in=enfants)
    riens = Question.objects.filter(parent=1)
    orphelins = [x for x in riens if x not in enfants and x not in parent_list]

    if request.method == 'POST':
        for question in question_list:
            assistant= request.user
            quest=Question.objects.get(pk=question.id)
            reponseaquestion = request.POST.get(str(question.id))
            if reponseaquestion:
                #reponse = Resultat.objects.create(reponsetexte = reponseaquestion)
                #Resultat.objects.update_or_create(personne=personne,question=quest,assistant=assistant,reponsetexte=reponseaquestion,)
                Resultat.objects.update_or_create(
                    # filter on the unique value of `upc`
                    personne=personne, question=quest, assistant=assistant,
                    # update these fields, or create a new object with these values
                    defaults={
                        'reponsetexte': reponseaquestion,
                    }
                )
        return render(request, 'save.html',
                                {'qid' : questionnaireid,
                                'orphelins' : orphelins,
                                'questions': question_list,
                                'enfants': enfant_list,
                                'parents': parent_list,
                                'pid' : personneid,
                                })
     #    url(r'^(?P<questionnaire>[0-9]+)/save/$', views.savereponses, name='savereponses'),
    else:
        return render(request, 'save.html',
                      {'qid' : questionnaireid,
                       'orphelins' : orphelins,
                       'questions': question_list,
                       'enfants': enfant_list,
                       'parents': parent_list,
                       'pid': personneid,
                       })

@login_required(login_url=settings.LOGIN_URI)
def savereponsesPhil(request, qid, pid):
    #affiche le formulaire pour 1 questionnaire et 1 personne
    questions =  Question.objects.filter(questionnaire__id=qid, parent__id=1)

    return render(
        request,
        'save2.html',
        {
            'qid': qid,
            'questions': questions,
            'pid': pid,
        }
    )

@login_required(login_url=settings.LOGIN_URI)
def savereponses(request, qid, pid):
    #affiche le formulaire pour 1 questionnaire et 1 personne

    questionstoutes = Question.objects.filter(questionnaire__id=qid)
    enfants = Question.objects.filter(question__parent__id__gt=1, questionnaire=qid)
    ascendancesM = {rquestion.id for rquestion in Question.objects.filter(pk__in=enfants)}
    ascendancesF = set()  #liste sans doublons
    for rquestion in questionstoutes:
        for fille in Question.objects.filter(parent__id=rquestion.id):
            # #va chercher si a des filles (question_ fille)
            ascendancesF.add(fille.id)

    return render(
        request,
        'save3.html',
        {
            'qid': qid,
            'pid': pid,
            'questions': questionstoutes,
            'ascendancesM': ascendancesM,
            'ascendancesF': ascendancesF,
            }
        )


@login_required(login_url=settings.LOGIN_URI)
def SelectPersonne(request):
    if request.method == 'POST':
        return redirect(savereponses,request.POST.get('questionnaireid'),
                                     request.POST.get('personneid')
                        )
    else:
         return render(
            request,
            'choix.html',
            {
                'personnes': Personne.objects.all(),
                'questionnaires': Questionnaire.objects.all()
            }
        )


@login_required(login_url=settings.LOGIN_URI)
def savereponsesdebug(request, qid, pid):
    #affiche le formulaire pour 1 questionnaire et 1 personne

    enfants = Question.objects.filter(question__parent__gt=1, questionnaire=qid)
    parent_list = Question.objects.filter(pk__in=enfants)

    questionstoutes =  Question.objects.filter(questionnaire__id=qid)
    ascendancesM = {}
    meresDeF = {}
    ascendancesF  = {}
    for rquestion in parent_list:
       ascendancesM[rquestion.id]='M'  # question_id = id de la fille, la mère = parent_cond

    for rquestion in questionstoutes:
       for fille in Question.objects.filter(parent__id=rquestion.id):
            # va chercher si a des filles (question_ fille)
            meresDeF[fille.id] = rquestion.id
            ascendancesF[fille.id]='F'

    return render(
        request,
        'save42.html',
        {
            'qid': qid,
            'questions': questionstoutes,
            'pid': pid,
            'ascendancesM': ascendancesM,
            'meresDeF':meresDeF,
            'ascendancesF': ascendancesF,
            }
        )