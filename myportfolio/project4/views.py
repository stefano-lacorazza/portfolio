from django.shortcuts import render
from .forms import UploadFileForm
#from django.http import HttpResponseRedirect
from .predict import predict
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
#import json 
#from .models import QR
# Create your views here.
def project4(request):
    form = UploadFileForm()

    return render(request, 'Project4/proyect4.html',  {'form': form})


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            #img_object = form.instance  
            img = form.cleaned_data.get("image")
            #obj = QR.objects.create(
            #                     img = img
            #                     )
            #obj.save()
            dict = predict(img)
            
            #context = {'hits': dict['hits'], 'imgs': json.dumps(dict['imgs']), 'urls': json.dumps(dict['urls'])}
            context = {'img':  img  }
            return render(request, "Project4/success4.html", context)
            #return render(request, "Project4/success4.html")
            #return HttpResponseRedirect("Project4/proyect4.html", context)
    else:
        form = UploadFileForm()
    return render(request, "Project4/success4.html")
