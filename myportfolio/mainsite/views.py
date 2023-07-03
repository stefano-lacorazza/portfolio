from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


def index(request):
  
    template = loader.get_template("mainsite\index.html")
    context = {
        "key": 0,
    }
    return render(request, 'mainsite\index.html', context)
def flight(request):
  
    template = loader.get_template("mainsite\fight.html")
    context = {
        "key": 0,
    }
    return render(request, 'mainsite\flight.html', context)