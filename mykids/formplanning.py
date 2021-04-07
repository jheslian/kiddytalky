
from django import forms
from main.models import Languagetolearn


class FormPlanning(forms):
    required_language = forms.Select()
    start_time_slot = forms.DateField()
    end_time_slot = forms.DateTimeField()
    date_slot = forms.DateTimeField()

    class Meta:
        model = Languagetolearn
        fields = ("date_slot", "start_time_slot", "end_time_slot")
