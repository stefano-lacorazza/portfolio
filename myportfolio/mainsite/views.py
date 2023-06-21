from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


def index(request):
  
    template = loader.get_template("mainsite/index.html")
    context = {
        "key": 0,
    }
    return render(request, "mainsite/index.html", context)