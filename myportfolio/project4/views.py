from django.shortcuts import render
from .forms import UploadFileForm
import pickle
import os
import pandas as pd
from django.http import HttpResponse
import requests

# Create your views here.
def project4(request):
    form = UploadFileForm()

    return render(request, 'Project4/proyect4.html',  {'form': form})


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})