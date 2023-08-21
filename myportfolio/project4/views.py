from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from .predict import predict

import json 

# Create your views here.
def project4(request):
    form = UploadFileForm()

    return render(request, 'Project4/proyect4.html',  {'form': form})


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            #dict = predict(request.FILES["image"])
            #context = {'hits': dict['hits'], 'imgs': json.dumps(dict['imgs']), 'urls': json.dumps(dict['urls'])}
            context = {'img': request.FILES["image"]}
            return HttpResponseRedirect("Project4/success4.html", context)
            #return HttpResponseRedirect("Project4/proyect4.html", context)
    else:
        form = UploadFileForm()
    return render(request, "Project4/success4.html")
