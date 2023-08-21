from django import forms



class UploadFileForm(forms.Form):
    image = forms.ImageField(label="Image file")
    #text = forms.CharField(label = 'text')
