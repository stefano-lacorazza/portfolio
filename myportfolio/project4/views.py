from django.shortcuts import render
from .forms import UploadFileForm
#from django.http import HttpResponseRedirect
from .predict import predict
from PIL import Image
#import json 
#from .models import QR
# Create your views here.
from roboflow import Roboflow
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
            #img = request.FILES["image"]
            #obj = QR.objects.create(
            #                     img = img
            #                     )
            #obj.save()
            #ource = r'C:\Users\laco-\OneDrive\Documentos\GitHub\portfolio\myportfolio\media'+str(img)
            #source = source.encode('unicode_escape')
            dict = predict(Image.open(img))
            #rf = Roboflow(api_key="PNtIMFu4RUL4mGqZc01W")
            #project = rf.workspace().project("qr-code-detector-jx362")
            #model = project.version(1).model
            #model.predict(source, confidence=40, overlap=30).save("prediction.jpg")
            #context = {'hits': dict['hits'], 'imgs': json.dumps(dict['imgs']), 'urls': json.dumps(dict['urls'])}
            context = dict
            return render(request, "Project4/success4.html", context)
            #return render(request, "Project4/success4.html")
            #return HttpResponseRedirect("Project4/proyect4.html", context)
    else:
        form = UploadFileForm()
    return render(request, "Project4/success4.html")
