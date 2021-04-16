from django import forms
from main.models import Child
from crum import get_current_user


class SelectForm(forms.ModelForm):
    """parent = get_current_user().id
    option = forms.ModelChoiceField(queryset=Child.objects.filter(user_id=parent.id))

    class Meta:
        model = Child
        fields = ['option']"""
