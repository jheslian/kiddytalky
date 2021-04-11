from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.cache import cache
from main.models import Child, User as MyCustomUser, Parent

"""def get_object(self):
    id_ = self.request.session['id_parent']
    print('id user: ', id_)
    parent = Parent.objects.get(user_id=id_)
    print('Objet user: ', parent)
    print("id du parent: ", parent.id)
    return parent.id"""
print("£CHILD PARENT ID:", cache.get('id_parent'))
class ChildRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    native_language = forms.CharField()
    birthdate = forms.DateField()
    #parent_id = forms.IntegerField(disabled=True, required=False)



    class Meta(UserCreationForm.Meta):
        model = MyCustomUser

    def get_parent_id(request):
        return request.session['id_parent']

    @transaction.atomic
    def save(self):
        print("111111111111",cache.get('id_parent'))
        print("22222222", cache.get('id_parent'))
        user = super().save(commit=False)
        user.is_child = True
        user.save()
        print("USER SAVED")
        child = Child.objects.create(user=user)
        child.first_name = self.cleaned_data.get('first_name')
        child.last_name = self.cleaned_data.get('last_name')
        child.native_language = self.cleaned_data.get('native_language')
        child.birthdate = self.cleaned_data.get('birthdate')
        child.parent_id = cache.get('id_parent')
        print("BEFORE CHILD SAVE")


        child.save()
        print("AFTER CHILD SAVE:", cache.get('id_parent'))


        return user



class EditChildInfo(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'birthdate', 'country', 'hobbies', 'description', 'language_to_learn']


