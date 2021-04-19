from main.models import Languagetolearn, Language, Child, Parent, Message
import datetime as dt
import django.http as rqt
from django.forms import ModelForm, DateInput, TimeInput, ChoiceField, Textarea
from django import forms
from django.core.validators import ValidationError, validate_slug
from crum import get_current_user

"""
forms.CharField(widget=forms.Textarea(attrs={"rows": 10, 'cols': 15}))
"""

