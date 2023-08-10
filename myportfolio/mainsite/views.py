from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


def index(request):

    
    context = {
        "key": 0,
    }
    return render(request, 'mainsite/index.html', context)


def proyect1(request):
  

    context = {
        "key": 0,
    }
    return render(request, 'mainsite/proyect1.html', context)
def proyect2(request):
  

    context = {
        "key": 0,
    }
    return render(request, 'mainsite/proyect2.html', context)



def proyect3(request):
  

    context = {
        "key": 0,
    }
    return render(request, 'mainsite/proyect3.html', context)