from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Document, Dossier
from .forms import DocumentForm, DossierForm
from django.conf import settings

@login_required(login_url=settings.LOGIN_URI)
def pardossier(request, pid):
    dossiercourant = Dossier.objects.get(pk=pid)
    dossiernom=dossiercourant.nomdossier
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            #newdoc = form.save(commit=False)
            newdoc.dossier = dossiercourant
            newdoc.save()

            return HttpResponseRedirect(reverse('dossier', args=[newdoc.dossier.id]))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the folder page
    enfants = Dossier.objects.all().filter(parentId=pid)
    parent = Dossier.objects.get(id=pid)
    documents = []
    for document in Document.objects.filter(dossier=pid):
        document.nicename = document.docfile.name.split('/')[-1]
        documents.append(document)

    return render(request, "depot/dossier.html", {'enfants': enfants,
                                                 'parent': parent,
                                                 'documents': documents,
                                                 'dossiernom': dossiernom,
                                                 'pid': pid,
                                                 'form': form, })
#    return render(request, "depot/dossier.html", {'enfants': enfants,
#                                                 'parent': parent,
#                                                 'documents': documents,
#                                                 'dossiernom': dossiernom,
#                                                 'pid': pid,
#                                                 'form': form,})


@login_required(login_url=settings.LOGIN_URI)
def dossier_new(request, pid):
    parent = Dossier.objects.get(pk=pid)
    if request.method == "POST":
        form = DossierForm(request.POST)
        if form.is_valid():
            dossier = form.save(commit=False)
            #dossier.comment = request.POST.get('comment', '')
            dossier.parentId = parent
            dossier.save()
            return HttpResponseRedirect(reverse('dossier', args=[dossier.id]))
    else:
        form = DossierForm()
    return render(request, "depot/dossier_edit.html", {'form': form,
                                                      'dossier_id': pid})