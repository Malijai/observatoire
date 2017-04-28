from django.shortcuts import render

# Create your views here.


def isManitoba(http_host):
   return True if 'ntpmb.ca' in http_host else False
   #return True

def accueil(request):
    if isManitoba(request.META.get('HTTP_HOST')):
        return render(request,'registration/logged_out.html')
    else:
        return render(request, "index.html")

