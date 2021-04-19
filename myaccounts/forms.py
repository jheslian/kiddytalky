from django import forms
from django.db import transaction
from main.models import Parent, Child
from datetime import datetime


class EditParentInfo(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1920, datetime.today().year)))


    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'birthdate', 'zipcode', 'street', 'country']

