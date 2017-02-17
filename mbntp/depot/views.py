from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document, Dossier
from .forms import DocumentForm, DossierForm


def pardossier(request, pid):

    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.dossier = Dossier.objects.get(pk=request.POST['dossier'])
            newdoc.save()

            return HttpResponseRedirect(reverse('dossier', args=[newdoc.dossier.id]))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the folder page
    enfants = Dossier.objects.all().filter(parentId=pid)
    parent = Dossier.objects.filter(id=pid)
    documents = []
    for document in Document.objects.filter(dossier=pid):
        document.nicename = document.docfile.name.split('/')[-1]
        documents.append(document)

    return render(request, "docs/dossier.html", {'enfants': enfants, 'parent': parent,'documents': documents, 'pid': pid, 'form': form,})


def dossier_new(request):
    if request.method == "POST":
        form = DossierForm(request.POST)
        if form.is_valid():
            dossier = form.save(commit=False)
            dossier.save()
            return HttpResponseRedirect(reverse('dossierslist'))
 #           return redirect('./docs/doclist.html')
    else:
        form = DossierForm()

    dossiers = Dossier.objects.all()

    return render(request, "docs/dossierslist.html", {'dossiers': dossiers, 'form': form})
