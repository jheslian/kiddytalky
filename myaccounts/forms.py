from django import forms
from main.models import Parent


class EditParentInfo(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['email',  'zipcode', 'street']