from django import forms
from . models import *

class MymodelForm(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields = ['name','description']