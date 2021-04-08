from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from main.models import *


class ParentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = models.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_parent = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Parent.objects.create(user=user)
        user.email = self.cleaned_data.get('email')
        customer.save()
        return user
    """email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "last_name", "first_name")
"""


class ChildRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    native_language = models.CharField()

    class Meta(UserCreationForm.Meta):
        model = User

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