from django.shortcuts import render
#from .forms import rentForm
import pickle
import os
import pandas as pd
from django.http import HttpResponse
from dash import Dash, html, dcc
from . import plotly_app

# Create your views here.
def project1(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    # if request.method == "POST":
    #     # create a form instance and populate it with data from the request:
    #     form = rentForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         model_path = os.path.join(os.path.dirname(__file__), 'rent_predictor_model.pkl')

    #         with open(model_path, 'rb') as model_file:
    #             model_RFR = pickle.load(model_file)
    #         apto = pd.DataFrame([[form.cleaned_data.get('city'),form.cleaned_data.get('built_Area'),form.cleaned_data.get('private_Area'),form.cleaned_data.get('stratum'),form.cleaned_data.get('rooms'),form.cleaned_data.get('parking_lots'),form.cleaned_data.get('bathrooms'),form.cleaned_data.get('age'),form.cleaned_data.get('lat'),form.cleaned_data.get('lon')]])
            
    #         # redirect to a new URL:
    #         return render(request, 'Project2\proyect2.html', {"form": 'The predicted rent cost is: $' +str(model_RFR.predict(pd.DataFrame(apto))[0])+' COP'})
    #     HttpResponse(model_RFR.predict(pd.DataFrame(apto)))

    # form = rentForm()
    # context = {
    #     "key": 0,
    # }
    return render(request, 'Project1/proyect1.html')
