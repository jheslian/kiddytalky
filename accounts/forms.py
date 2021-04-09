from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from main.models import Parent, User as MyCustomUser, Child


class ParentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    birthdate = forms.DateField(required=True)
    zipcode = forms.CharField(required=True)
    street = forms.CharField(required=True)
    country = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = MyCustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True

        user.save()
        parent = Parent.objects.create(user=user)
        parent.email = self.cleaned_data.get('emailEERR')
        parent.zipcode = self.cleaned_data.get('zipcode')
        parent.street = self.cleaned_data.get('street')
        parent.country = self.cleaned_data.get('country')
        parent.first_name = self.cleaned_data.get('first_name')
        parent.last_name = self.cleaned_data.get('last_name')
        parent.birthdate = self.cleaned_data.get('birthdate')
        parent.save()
        return user




class ChildRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    native_language = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = MyCustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_child = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Child.objects.create(user=user)
        user.last_name = self.cleaned_data.get('email')
        customer.save()
        return user
