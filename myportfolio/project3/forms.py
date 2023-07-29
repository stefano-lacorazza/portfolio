from django import forms


class fileForm(forms.Form):
  
    file = forms.FileField(label = 'Please upload your whatsapp chat')
