from django import forms
from django.db import transaction
from main.models import Parent, Child


class EditParentInfo(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'birthdate', 'zipcode', 'street', 'country']

