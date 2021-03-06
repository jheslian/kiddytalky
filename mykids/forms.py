from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.cache import cache
from main.models import Child, User as MyCustomUser, Parent, Language, Country
from django.contrib.sessions.models import Session
from django.utils import timezone
from crum import get_current_user
from datetime import  datetime
from django.forms.widgets import Input, PasswordInput

"""def get_object(self):
    id_ = self.request.session['id_parent']
    print('id user: ', id_)
    parent = Parent.objects.get(user_id=id_)
    print('Objet user: ', parent)
    print("id du parent: ", parent.id)
    return parent.id"""



class ChildRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}) )
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range((datetime.today().year)-15, (datetime.today().year)-8)))
    native_language = forms.ModelChoiceField(queryset=Language.objects.all(), empty_label="Language")
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Country")
    # language = forms.ModelChoiceField(queryset=Language.objects.all(), label="Wish to learn", empty_label="Language")





    class Meta(UserCreationForm.Meta):
        model = MyCustomUser


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_child = True
        user.save()
        child = Child.objects.create(user=user)
        child.first_name = self.cleaned_data.get('first_name')
        child.last_name = self.cleaned_data.get('last_name')
        child.native_language = self.cleaned_data.get('native_language')
        child.birthdate = self.cleaned_data.get('birthdate')
        user_id = get_current_user().id
        parent = Parent.objects.get(user_id=user_id)
        child.parent_id = parent.id
        #child.language_id = self.cleaned_data.get('language')
        child.country_id=self.cleaned_data.get('country')

        child.save()

        return user


class EditChildInfo(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range((datetime.today().year)-15, (datetime.today().year)-8)))

    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'birthdate', 'country', 'hobbies', 'description']
