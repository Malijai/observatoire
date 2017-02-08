from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from .forms import CommentaireForm, EntreeForm
from .models import Entree
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class BlogIndex(generic.ListView):
    template_name = 'blogindex.html'

    def get_queryset(self):
        return Entree.objects.filter(posted__lte=timezone.now()).order_by('-posted')[:5]

class BlogDetail(generic.DetailView):
    template_name = 'blogdetail.html'
    model = Entree

def listing(request):
    post_list = Entree.objects.all()
    paginator = Paginator(post_list, 3) # Show 3 post par page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'posts': posts})

def commentaire_new(request, pk):
#    posttitre = ''
    blabla = Entree.objects.get(pk=pk)
    posttitre=blabla.titre_en
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.entree = Entree.objects.get(pk=pk)
            #post.author = request.user
            #commentaire.posted = timezone.now()
            commentaire.save()
            return redirect('blogdetail', pk=pk)
    else:
        form = CommentaireForm()
    return render(request, "blog/commentaire_edit.html", {'form': form,  
                                                        'post_id': pk,
                                                        'Posttitre':  posttitre})
def entree_new(request):
    if request.method == "POST":
        form = EntreeForm(request.POST)
        if form.is_valid():
            entree = form.save(commit=False)
            #entree.author = request.user
            #commentaire.posted = timezone.now()
            entree.save()
            return redirect('blogdetail', entree.id)
    else:
        form = EntreeForm()
    return render(request, "blog/entree_edit.html", {'form': form})



def test(request):
    return render(request, 'test.html')
