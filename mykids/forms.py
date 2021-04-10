from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from main.models import Child, User as MyCustomUser


class EditChildInfo(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'birthdate', 'country', 'hobbies', 'description', 'language_to_learn']


class ChildRegistrationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    native_language = forms.CharField()
    birthdate = forms.DateField()

    class Meta(UserCreationForm.Meta):
        model = MyCustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_child = True
        user.save()
        child = Child.objects.create(user=user)
        #child.parent_id = Parent.objects.get(id=id)
        child.first_name = self.cleaned_data.get('first_name')
        child.last_name = self.cleaned_data.get('last_name')
        child.native_language = self.cleaned_data.get('native_language')
        child.birthdate = self.cleaned_data.get('birthdate')
        child.save()
        return user