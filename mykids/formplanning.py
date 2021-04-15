from main.models import Languagetolearn, Language, Child, Parent
import datetime as dt
import django.http as rqt
from django.forms import ModelForm, DateInput, TimeInput, ChoiceField
from django import forms
from django.core.validators import ValidationError, validate_slug
from crum import get_current_user


# from calendarapp.models import EventMember

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
            'child_correspondent': forms.HiddenInput(),
            'correspondent_language': forms.HiddenInput(),
            'validation_status': forms.HiddenInput(),
            'link_video': forms.HiddenInput(),
            'meeting_id': forms.HiddenInput()

        }

        exclude = ['last_name']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['date_slot'].input_formats = ('%Y-%m-%d',)
        self.fields['start_time_slot'].input_formats = ('%H:%M',)
        self.fields['end_time_slot'].input_formats = ('%H:%M',)
        self.fields['language'].queryset = Language.objects.all()
        self.fields['child_correspondent'].queryset = Child.objects.filter(parent_id=1)





    def clean_date_slot(self):
        date_slot = self.cleaned_data['date_slot']

        if date_slot < dt.date.today():
            raise ValidationError('test')
        return date_slot
