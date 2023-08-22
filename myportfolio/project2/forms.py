from django import forms


city_Choices = (
    ('0', 'Bogotá'), ( '1','Barranquilla'), ( '4','Medellín'), ('5','Cali'), ('6','Santa Marta'), ('7','Cartagena'), 
 ('8','Pereira'), ( '9','Bucaramanga'), ('10','Montería'),('11','Envigado'),('12','Villavicencio'),( '99','Otro') 
)   
class rentForm(forms.Form):
    city = forms.ChoiceField(label="City", choices =city_Choices )
    address = forms.CharField(label='Property address')
    built_Area = forms.IntegerField(label='Buit area in m2')
    private_Area = forms.IntegerField(label='Total area in m2')
    stratum = forms.IntegerField(label = 'Estrato' )
    rooms = forms.IntegerField(label = 'Number of rooms' )
    parking_lots = forms.IntegerField(label = 'Number of parking lots' )
    bathrooms = forms.IntegerField(label = 'Number of bathrooms')
    age = forms.IntegerField(label = 'Age of the property in years')
    
