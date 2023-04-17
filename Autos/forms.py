from django import forms

class BuscarAutoForm(forms.Form):
    criterio = forms.CharField(max_length=20)