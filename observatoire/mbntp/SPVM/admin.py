from __future__ import unicode_literals
from django.contrib import admin

from .models import Typequestion, Questionnaire,Question,Condition,Province,Personne,Resultat

admin.site.register(Typequestion)
admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Condition)
admin.site.register(Province)
admin.site.register(Personne)
admin.site.register(Resultat)