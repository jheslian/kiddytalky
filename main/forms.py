from django import forms
from .models import Child, Languagetolearn


class MeetingValidationForm(forms.ModelForm):

    class Meta:
        model = Languagetolearn


        fields = ['child_correspondent']




