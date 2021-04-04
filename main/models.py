from django.db import models


# Create your models here.
class Parent(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100) #editable=False
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birthdate = models.DateTimeField()
    street = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=100,  default='USA')

    def __str__(self):
        return self.email


class Language(models.Model):
    language_choices = [
        ('English', 'English'),
        ('Mandarin', 'Mandarin'),
        ('Spanish', 'Spanish')
    ]
    name = models.CharField(choices=language_choices, max_length=100, unique=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    pseudo = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='') # editable=False,
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
    native_language = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    #languagetolearn = models.ManyToManyField(Language, blank=True)
    """language_choices = [
        ('English', 'English'),
        ('Mandarin', 'Mandarin'),
        ('Spanish', 'Spanish')
    ]
    language_to_learn = models.CharField(choices=language_choices, max_length=100, default="English")"""

    def __str__(self):
        return self.pseudo



class Visio(models.Model):
    child_participant = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='child_participant')
    child_correspondent = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='child_correspondent')
    # participant_language = models.ForeignKey(Child, to_fields="language_to_learn", on_delete=models.CASCADE, related_name="participant_language") # related_name="participant_language"
    # correspondent_language = models.ForeignKey(Child, to_fields="language_to_learn", on_delete=models.CASCADE, related_name='correspondent_language') # related_name='correspondent_language'
    participant_language = models.ForeignKey(Language, on_delete=models.CASCADE, default='', related_name="participant_language") # related_name="participant_language"
    correspondent_language = models.ForeignKey(Language, default='', on_delete=models.CASCADE, related_name='correspondent_language') # related_name='correspondent_language'
    visio_start = models.DateTimeField()
    visio_end = models.DateTimeField()
    visio_date = models.DateTimeField()
    status_choice = [('Pending', 'Pending'), ('Confirmed', 'Confirmed')]
    validation_status = models.CharField(max_length=10, choices=status_choice)

    def __str__(self):
        return self.visio_date


class Message(models.Model):
    message_to = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_to')
    message_from = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_from')
    message_date = models.DateTimeField('date sent')
    content = models.TextField()

    def __str__(self):
        return self.message_date








