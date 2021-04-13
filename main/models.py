from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Language(models.Model):
    """language_choices = [
        ('English', 'English'),
        ('Mandarin', 'Mandarin'),
        ('Spanish', 'Spanish')
    ]
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('main:myaccounts:my-account', kwargs={"id": self.id})

    def get_url_signup_parent(self):
        return reverse('main:accounts:parent-register')

    def get_absolute_child_url(self):
        return reverse("main:mykids:child-view", kwargs={"id": self.id})

    def get_absolute_childlist_url(self):
        return reverse("main:mykids:kids", kwargs={"id": self.id})



class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    last_name = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    birthdate = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=100, default='USA')
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('main:myaccounts:my-account', kwargs={"id": self.id})

    def get_success_url(self):
        user_id = self.kwargs.get('id')
        return reverse('myaccounts:my-account', kwargs={'id':user_id})

class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, blank=True, default='')
    first_name = models.CharField(max_length=100, default='')
    birthdate = models.DateTimeField(null=True)
    native_language = models.CharField(max_length=100, default="")
    hobbies = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    #language_to_learn = models.ManyToManyField(Language, default="")
    language_choices = [
        ('English', 'English'),
        ('Mandarin', 'Mandarin'),
        ('Spanish', 'Spanish')
    ]
    language_to_learn = models.CharField(choices=language_choices, max_length=100, default='')
    # date_joined = models.DateField(auto_now_add=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, default=0, blank=True)

    def get_absolute_url(self):
        return reverse("main:mykids:child-view", kwargs={"id": self.id})


"""
class Visio(models.Model):
    child_participant = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='child_participant')
    child_correspondent = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='child_correspondent')
    participant_language = models.ForeignKey(Language, on_delete=models.CASCADE, default='English',
                                             related_name="participant_language")
    correspondent_language = models.ForeignKey(Language, default='', on_delete=models.CASCADE,
                                               related_name='correspondent_language')
    visio_start = models.DateTimeField()
    visio_end = models.DateTimeField()
    visio_date = models.DateTimeField(auto_now=True)
    status_choice = [('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')]
    validation_status = models.CharField(max_length=10, choices=status_choice)

    def __str__(self):
        return self.visio_date


class Message(models.Model):
    message_to = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_to')
    message_from = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_from')
    message_date = models.DateTimeField('date sent', auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.message_date

"""
