from django.contrib import admin

from .models import Contact

# Register your models here.

class SuiviAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification', {'fields': ['nom', 'prenom', 'affiliation','courriel','domaine']}),
        ('Envoi lettre', {'fields': ['responsable', 'envoifait']}),
        ('Reponse', {'fields': ['reponse']}),
    ]

    list_display = ('nom', 'prenom','responsable', 'envoifait','reponse')

    list_filter = ['nom']

    def save_model(self, request, obj, form, change):
        obj.entrepar = request.user
        obj.save()

admin.site.register(Contact, SuiviAdmin)

