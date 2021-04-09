from django import forms
from django.db import transaction
from main.models import Parent, User as MyCustomUser

"""
class EditParentInfo(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['email', 'zipcode', 'street']

"""


class EditParentInfo(forms.ModelForm):
    """   first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    birthdate = forms.DateField(required=False)
    """
    """ zipcode = forms.CharField(required=False)
    street = forms.CharField(required=False)
    country = forms.CharField(required=False)"""

    """class Meta:
        model = Parent
        fields =[ 'first_name', 'last_name','email', 'birthdate', 'zipcode', 'street', 'country']
"""
    #first_name = forms.CharField(required=False)
    #last_name = forms.CharField(required=False)
    #email = forms.EmailField()
    #birthdate = forms.DateField(required=False)
    #country = forms.CharField(required=False)
    class Meta:
        model = Parent
        fields = ['first_name', 'last_name', 'birthdate', 'zipcode', 'street', 'country']

    """    def refresh_from_db(self, using=None, fields=None, **kwargs):
        # fields contains the name of the deferred field to be
        # loaded.
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            # If any deferred field is going to be loaded
            if fields.intersection(deferred_fields):
                # then load all of them
                fields = fields.union(deferred_fields)
                fields.update()
        super().refresh_from_db(using, fields, **kwargs)"""