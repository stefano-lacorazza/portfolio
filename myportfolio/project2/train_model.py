import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.ensemble import RandomForestRegressor
import pickle

def city_cleaner(txt):
    
    if 'Bogotá' in txt or 'Bogota' in txt:
        return '0'
    elif 'Barranquilla' in txt:
        return '1'
    elif 'Medellín' in txt:
        return '4'
    elif 'Cali' in txt:
        return '5'
    elif 'Santa Marta' in txt:
        return '6'
    elif 'Cartagena' in txt:
        return '7'
    elif 'Pereira' in txt:
        return '8' 
    elif 'Bucaramanga' in txt:
        return '9'
    elif 'Montería' in txt:
        return '10'
    elif 'Envigado' in txt:
        return '11'
    elif 'Villavicencio' in txt:
        return '12'
    elif 'Manizales' in txt:
        return '13'
    else:return '99'
        

def train_model():

    dataset = pd.read_csv("C:/Users/laco-/OneDrive/Documentos/GitHub/portfolio/myportfolio/project2/frame.csv")
    dataset = dataset.drop(columns = [ 'Barrio', 'Unnamed: 0', 'Codigo Web', 'Titulo', 'Barrio Catastral','Precio venta', 'Zona', 'Sector','Interior', 'Exterior',  'Direccion', 'Url'])
    dataset = dataset.drop([0])
    dataset['Long'] = dataset['Long'].replace([0],[np.nan])
    dataset['Lat'] = dataset['Lat'].replace([0],[np.nan])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace(['Más de 20 años'],[25])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace(['Entre 5 y 10 años'],[7])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace(['Entre 10 y 20 años'],[15])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace(['Entre 0 y 5 años'],[2])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace(['Entre 10 y 20 año'],[15])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace(['Remodelado'],[0])
    dataset['Antiguedad'] = dataset['Antiguedad'].replace([np.nan],[0])
    dataset = dataset.dropna()
    dataset['Precio arriendo'] = dataset['Precio arriendo'].apply(lambda x: x.replace('$', ''))
    dataset['Precio arriendo'] = dataset['Precio arriendo'].apply(lambda x: x.replace('.', ''))
    dataset['Ciudad'] = dataset['Ciudad'].apply(lambda x: city_cleaner(x))
    dataset['Estrato'] = dataset['Estrato'].apply(lambda x: x.replace('Comercial', '0'))
    X = dataset.drop(['Precio arriendo'], axis=1)
    Y = dataset['Precio arriendo']
    X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=0)
    model_RFR = RandomForestRegressor(n_estimators=100)
    model_RFR.fit(X_train, Y_train)
    Y_pred = model_RFR.predict(X_valid)
    print("Accuracy:", mean_absolute_percentage_error(Y_valid, Y_pred))
    # Save the model and vectorizer
 
    with open('rent_predictor_model.pkl', 'wb') as model_file:
        pickle.dump(model_RFR, model_file)
   

if __name__ == "__main__":
    train_model()