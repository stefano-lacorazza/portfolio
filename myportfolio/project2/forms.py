from django import forms

city_Choices = (
    ('Bogotá', 'Bogotá'), ('Barranquilla', 'Barranquilla'), ('Medellín', 'Medellín'), ('Cali', 'Cali'), ('Santa Marta', 'Santa Marta'), ('Cartagena', 'Cartagena'), 
 ('Pereira', 'Pereira'), ('Bucaramanga', 'Bucaramanga'), ('Montería', 'Montería'),('Envigado', 'Envigado'),('Villavicencio', 'Villavicencio'),('Otro', 'Otro') 
)   
class rentForm(forms.Form):
    City = forms.ChoiceField(label="City", choices =city_Choices )