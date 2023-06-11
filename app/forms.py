from django import forms
from sih_app.models import emp,nsapdata, otherdata

class nsapform(forms.ModelForm):
    class Meta:
        model=nsapdata
        fields="__all__"
class othersform(forms.ModelForm):
    class Meta:
        model=otherdata
        fields="__all__"
class empform(forms.ModelForm):
    class Meta:
        model=emp
        fields="__all__"