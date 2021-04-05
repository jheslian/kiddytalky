from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from main.models import Parent, Child


class ParentRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    #birthdate = forms.DateInput

    class Meta:
        model = Parent
        fields = ("email", "password1", "password2", "last_name", "first_name", "birthdate", "zipcode", "country")
        #widgets = {'birthdate': forms.DateInput(attrs=DateInput)}


"""class DateInput(forms.DateInput):
    input_type = 'date'"""