from django.shortcuts import render

# Create your views here.


def indexMB(request):
    return render(request, "indexmb/index.html")