from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.cache import cache
from main.models import Child, User as MyCustomUser, Parent, Language
from django.contrib.sessions.models import Session
from django.utils import timezone
from crum import get_current_user

"""def get_object(self):
    id_ = self.request.session['id_parent']
    print('id user: ', id_)
    parent = Parent.objects.get(user_id=id_)
    print('Objet user: ', parent)
    print("id du parent: ", parent.id)
    return parent.id"""



class ChildRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    native_language = forms.CharField()
    birthdate = forms.DateField()
    language = forms.ModelChoiceField(queryset=Language.objects.all())


    #def __init__(self):


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
        child.language_id = self.cleaned_data.get('language')

        child.save()


        return user


class EditChildInfo(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'birthdate', 'language', 'country', 'hobbies', 'description']
