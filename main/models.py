from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser


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


class Parent(AbstractBaseUser):
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=100) #editable=False
    last_name = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    birthdate = models.DateTimeField(null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, default='USA')
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name', 'country']

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        # return reverse("accounts:parent-detail", kwargs={"id": self.id})
        return reverse("accounts:parent-detail", kwargs={"id": self.id})

    """ def get_success_url(self):
        return '/'
    """


class Child(AbstractBaseUser):
    pseudo = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
    native_language = models.CharField(max_length=100, default="English")
    hobbies = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    # languagetolearn = models.ManyToManyField(Language, default="English")
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pseudo


class Languagetolearn(models.Model):
    TITLE_CHOICES = [
        ('An', 'Anglais.'),
        ('Fr', 'Français.'),
        ('All', 'Allemdand'),
    ]
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    id_child = models.ForeignKey(Child, on_delete=models.CASCADE)
    id_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_slot = models.DateField()
    start_time_slot = models.TimeField()
    end_time_slot = models.TimeField()


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
