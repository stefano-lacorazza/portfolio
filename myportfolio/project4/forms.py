from django import forms
#from django.db import models  
from .models import UploadImage  

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image',] 
    image = forms.ImageField(label="Image file")
    
    #class Meta:
    #    model = UploadImage 
    #    fields = ('image', )
