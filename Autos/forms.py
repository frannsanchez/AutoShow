from django import forms

class BuscarAutoForm(forms.Form):
    criterio_marca = forms.CharField(max_length=20)