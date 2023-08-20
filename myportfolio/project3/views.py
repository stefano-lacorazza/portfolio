from django.shortcuts import render
from .forms import fileForm
import re

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from django.http import HttpResponse

def project3(request):

     
        

    return render(request, 'Project3/proyect3.html')