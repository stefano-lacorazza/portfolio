from django.shortcuts import render
from .forms import rentForm
import pickle
import os
import pandas as pd
from django.http import HttpResponse
import requests
# Create your views here.
def project2(request):


    if request.method == "POST":
        
        # create a form instance and populate it with data from the request:
        form = rentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            model_path = os.path.join(os.path.dirname(__file__), 'rent_predictor_model.pkl')
            address = form.cleaned_data.get('address').join('%20').join(form.cleaned_data.get('city')).replace(' ','%20').replace('#','%23')
            api_key = 'AIzaSyB7ll_7odkimkj8vly0VIt-Dol9useuv5Q'
            
            api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
            api_response_dict = api_response.json()

            if api_response_dict['status'] == 'OK':
                latitude = api_response_dict['results'][0]['geometry']['location']['lat']
                longitude = api_response_dict['results'][0]['geometry']['location']['lng']
                HttpResponse(''.join(latitude).join(' ').join(longitude))
            with open(model_path, 'rb') as model_file:
                model_RFR = pickle.load(model_file)
            apto = pd.DataFrame([[form.cleaned_data.get('city'),form.cleaned_data.get('built_Area'),form.cleaned_data.get('private_Area'),form.cleaned_data.get('stratum'),form.cleaned_data.get('rooms'),form.cleaned_data.get('parking_lots'),form.cleaned_data.get('bathrooms'),form.cleaned_data.get('age'),latitude,longitude]])
            
            # redirect to a new URL:
            return render(request, 'Project2/proyect2.html', {"form": form , "prediction": '$' +str(model_RFR.predict(pd.DataFrame(apto))[0])+' COP'})
        HttpResponse(model_RFR.predict(pd.DataFrame(apto)))

    form = rentForm()
    context = {
        "key": 0,
    }
    return render(request, 'Project2/proyect2.html',  {'form': form})

