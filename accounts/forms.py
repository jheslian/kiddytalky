from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from main.models import Parent


class ParentRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Parent
        fields = ("username","email", "password1", "password2", "last_name", "first_name", "birthdate", "zipcode", "country")
