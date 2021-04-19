from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from main.models import Parent, User as MyCustomUser, Language , Country
from datetime import datetime


class ParentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1920, datetime.today().year)))
    zipcode = forms.CharField(required=True)
    street = forms.CharField(required=True)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Country")




    class Meta(UserCreationForm.Meta):
        model = MyCustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.save()
        parent = Parent.objects.create(user=user)
        parent.email = self.cleaned_data.get('email')
        parent.zipcode = self.cleaned_data.get('zipcode')
        parent.street = self.cleaned_data.get('street')
        parent.country_id = self.cleaned_data.get('country')
        parent.first_name = self.cleaned_data.get('first_name')
        parent.last_name = self.cleaned_data.get('last_name')
        parent.birthdate = self.cleaned_data.get('birthdate')
        parent.save()
        return user



