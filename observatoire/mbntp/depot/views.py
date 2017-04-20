from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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
            # newdoc.dossier = Dossier.objects.get(pk=request.POST['dossier'])
            newdoc.comment = request.POST.get('comment', '')
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

def home(request):
    documents = Document.objects.all()
    return render(request, 'depot/home.html', { 'documents': documents })

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'depot/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'depot/simple_upload.html')
