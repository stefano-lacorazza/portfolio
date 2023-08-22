from django.shortcuts import render
from .forms import UploadFileForm
#from django.http import HttpResponseRedirect
from .predict import predict
from PIL import Image
#import json 
#from .models import QR
# Create your views here.
from roboflow import Roboflow
from .models import UploadImage  
def project4(request):
    form = UploadFileForm()
    

    return render(request, 'Project4/proyect4.html',  {'form': form})


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #img = form.cleaned_data.get("image")
            nimage = UploadImage(image = request.FILES['image'])
            nimage.image.name
           #f = Image.open(img)
            dict = predict(nimage.image.name)
           # f.close()
         
            context = dict
            #context ={'urls': [nimage.image.path]}
            return render(request, "Project4/success4.html", context)

    else:
        form = UploadFileForm()
    return render(request, "Project4/success4.html")
