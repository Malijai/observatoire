from django.contrib import admin
from .models import Document,Dossier
# Register your models here.

class DepotFichiers(admin.ModelAdmin):
    fieldsets = [
        ('fichiers', {'fields': ['nicename', 'docfile','comment','author',]}),
        ('Dossier', {'fields': ['dossier',]}),
    ]

    list_display = ('nicename', 'comment','posted')

    list_filter = ['dossier','author','posted']

    def save_model(self, request, obj, form, change):
        obj.save()

class DepotDossiers(admin.ModelAdmin):
    list_display = ('nomdossier', 'comment')

    list_filter = ['parentId']

    def save_model(self, request, obj, form, change):
        obj.save()

admin.site.register(Document, DepotFichiers)
admin.site.register(Dossier, DepotDossiers)
