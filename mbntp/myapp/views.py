from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Document, Dossier
from .forms import DocumentForm, DossierForm


def doclist(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.dossier = Dossier.objects.get(pk=request.POST['dossier'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('doclist'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = []
    for document in Document.objects.all():
        document.nicename = document.docfile.name.split('/')[-1]
        documents.append(document)

    dossiers = []
    for dossier in Dossier.objects.all():
        documents = []
        for document in Document.objects.filter(dossier=dossier):
            document.nicename = document.docfile.name.split('/')[-1]
            documents.append(document)
            dossiers.append(
            dict(
                dossier=dossier,
                documents=documents,
            )
        )


    # Render list page with the documents and the form
    return render(
        request,
        'doclist.html',
        {'dossiers': dossiers, 'form': form}
)

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