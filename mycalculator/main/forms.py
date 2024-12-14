from django import forms

class HomeForm(forms.Form):
    number1 = forms.FloatField(required=False)
    number2 = forms.FloatField(required=False)
    number3 = forms.FloatField(required=False)
    number4 = forms.FloatField(required=False)
