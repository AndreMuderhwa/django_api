from django.forms import ModelForm
from Mobile_App.models import *

class PartiPolitiqueForm(ModelForm):
    class Meta:
        model=PartiPolitique
        fields="__all__"