
from main.models import Languagetolearn, Language, Child
import datetime as dt

from django.forms import ModelForm, DateInput, TimeInput,ChoiceField
#from calendarapp.models import EventMember
from django import forms
from django.core.validators import ValidationError, validate_slug


# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# ---------------------------------------------------
# model form of model event
# ---------------------------------------------------
class EventForm(ModelForm):
    class Meta:
        model = Languagetolearn

        fields = '__all__'


        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {

            'date_slot': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'start_time_slot': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'end_time_slot': TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            #'language': ChoiceField(queryset=Language.objects.all())

        }

        # exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['date_slot'].input_formats = ('%Y-%m-%d',)
        self.fields['start_time_slot'].input_formats = ('%H:%M',)
        self.fields['end_time_slot'].input_formats = ('%H:%M',)
        self.fields['language'].queryset=Language.objects.all()
        self.fields['language'].queryset = Language.objects.all()
        self.fields['last_name'].queryset = Child.objects.filter(parent_id=2)

    def clean_date_slot(self):

        date_slot = self.cleaned_data['date_slot']

        if date_slot < dt.date.today():
            raise ValidationError('test')
        return date_slot

# ---------------------------------------------------
# ---------------------------------------------------

"""
class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ['user']



class FormPlanning(forms):
    required_language = forms.Select()
    start_time_slot = forms.DateField()
    end_time_slot = forms.DateTimeField()
    date_slot = forms.DateTimeField()

    class Meta:
        model = Languagetolearn
        fields = ("date_slot", "start_time_slot", "end_time_slot")

"""
