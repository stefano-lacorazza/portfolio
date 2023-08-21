from django import forms
from django.db import models  
from .models import UploadImage  

class UploadFileForm(forms.ModelForm):
    model = UploadImage
    image = forms.ImageField(label="Image file")
    #fields = '__all__'  
