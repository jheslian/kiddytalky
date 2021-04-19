from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

class Country(models.Model):
    country_choices = [
        ('Afghanistan', 'Afghanistan'),
        ('Albania', 'Albania'),
        ('Algeria', 'Algeria'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('The Bahamas', 'The Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cape Verde', 'Cape Verde'),
        ('Central African Republic', 'Central African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo', 'Congo'),
        ('Costa Rica', 'Costa Rica'),
        ('Cote d\'Ivoire', 'Cote d\'Ivoire'),
        ('Croatia', 'Croatia'),
        ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'),
        ('East Timor ', 'East Timor '),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('The Gambia', 'The Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Ghana', 'Ghana'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guatemala', 'Guatemala'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea North', 'Korea North'),
        ('Korea South', 'Korea South'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Laos', 'Laos'),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macedonia', 'Macedonia'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Moldova', 'Moldova'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Romania', 'Romania'),
        ('Russia', 'Russia'),
        ('Rwanda', 'Rwanda'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('South Sudan', 'South Sudan'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Syria', 'Syria'),
        ('Taiwan', 'Taiwan'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States of America', 'United States of America'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe')
    ]
    name = models.CharField(choices=country_choices, max_length=100, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    language_choices = [
        ('Afrikaans', 'Afrikaans'),
        ('Albanian', 'Albanian'),
        ('Amharic', 'Amharic'),
        ('Arabic - Egyptian Spoken', 'Arabic - Egyptian Spoken'),
        ('Arabic - Levantine', 'Arabic - Levantine'),
        ('Arabic - Modern Standard', 'Arabic - Modern Standard'),
        ('Arabic - Moroccan Spoken', 'Arabic - Moroccan Spoken'),
        ('Arabic - Overview', 'Arabic - Overview'),
        ('Aramaic', 'Aramaic'),
        ('Armenian', 'Armenian'),
        ('Assamese', 'Assamese'),
        ('Aymara', 'Aymara'),
        ('Azerbaijani', 'Azerbaijani'),
        ('Balochi', 'Balochi'),
        ('Bamanankan', 'Bamanankan'),
        ('Bashkort (Bashkir)', 'Bashkort (Bashkir)'),
        ('Basque', 'Basque'),
        ('Belarusan', 'Belarusan'),
        ('Bengali', 'Bengali'),
        ('Bhojpuri', 'Bhojpuri'),
        ('Bislama', 'Bislama'),
        ('Bosnian', 'Bosnian'),
        ('Brahui', 'Brahui'),
        ('Bulgarian', 'Bulgarian'),
        ('Burmese', 'Burmese'),
        ('Cantonese', 'Cantonese'),
        ('Catalan', 'Catalan'),
        ('Cebuano', 'Cebuano'),
        ('Chechen', 'Chechen'),
        ('Cherokee', 'Cherokee'),
        ('Croatian', 'Croatian'),
        ('Czech', 'Czech'),
        ('Dakota', 'Dakota'),
        ('Danish', 'Danish'),
        ('Dari', 'Dari'),
        ('Dholuo', 'Dholuo'),
        ('Dutch', 'Dutch'),
        ('English', 'English'),
        ('Esperanto', 'Esperanto'),
        ('Estonian', 'Estonian'),
        ('Éwé', 'Éwé'),
        ('Finnish', 'Finnish'),
        ('French', 'French'),
        ('Georgian', 'Georgian'),
        ('German', 'German'),
        ('Gikuyu', 'Gikuyu'),
        ('Greek', 'Greek'),
        ('Guarani', 'Guarani'),
        ('Gujarati', 'Gujarati'),
        ('Haitian Creole', 'Haitian Creole'),
        ('Hausa', 'Hausa'),
        ('Hawaiian', 'Hawaiian'),
        ('Hawaiian Creole', 'Hawaiian Creole'),
        ('Hebrew', 'Hebrew'),
        ('Hiligaynon', 'Hiligaynon'),
        ('Hindi', 'Hindi'),
        ('Hungarian', 'Hungarian'),
        ('Icelandic', 'Icelandic'),
        ('Igbo', 'Igbo'),
        ('Ilocano', 'Ilocano'),
        ('Indonesian ', 'Indonesian '),
        ('Inuit/Inupiaq', 'Inuit/Inupiaq'),
        ('Irish Gaelic', 'Irish Gaelic'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('Jarai', 'Jarai'),
        ('Javanese', 'Javanese'),
        ('K’iche’', 'K’iche’'),
        ('Kabyle', 'Kabyle'),
        ('Kannada', 'Kannada'),
        ('Kashmiri', 'Kashmiri'),
        ('Kazakh', 'Kazakh'),
        ('Khmer', 'Khmer'),
        ('Khoekhoe', 'Khoekhoe'),
        ('Korean', 'Korean'),
        ('Kurdish', 'Kurdish'),
        ('Kyrgyz', 'Kyrgyz'),
        ('Lao', 'Lao'),
        ('Latin', 'Latin'),
        ('Latvian', 'Latvian'),
        ('Lingala', 'Lingala'),
        ('Lithuanian', 'Lithuanian'),
        ('Macedonian', 'Macedonian'),
        ('Maithili', 'Maithili'),
        ('Malagasy', 'Malagasy'),
        ('Malay', 'Malay'),
        ('Malayalam', 'Malayalam'),
        ('Mandarin ', 'Mandarin '),
        ('Marathi', 'Marathi'),
        ('Mende', 'Mende'),
        ('Mongolian', 'Mongolian'),
        ('Nahuatl', 'Nahuatl'),
        ('Navajo', 'Navajo'),
        ('Nepali', 'Nepali'),
        ('Norwegian', 'Norwegian'),
        ('Ojibwa', 'Ojibwa'),
        ('Oriya', 'Oriya'),
        ('Oromo', 'Oromo'),
        ('Pashto', 'Pashto'),
        ('Persian', 'Persian'),
        ('Polish', 'Polish'),
        ('Portuguese', 'Portuguese'),
        ('Punjabi', 'Punjabi'),
        ('Quechua', 'Quechua'),
        ('Romani', 'Romani'),
        ('Romanian', 'Romanian'),
        ('Russian', 'Russian'),
        ('Rwanda', 'Rwanda'),
        ('Samoan', 'Samoan'),
        ('Sanskrit', 'Sanskrit'),
        ('Serbian', 'Serbian'),
        ('Shona', 'Shona'),
        ('Sindhi', 'Sindhi'),
        ('Sinhala', 'Sinhala'),
        ('Slovak', 'Slovak'),
        ('Slovene', 'Slovene'),
        ('Somali', 'Somali'),
        ('Spanish', 'Spanish'),
        ('Swahili', 'Swahili'),
        ('Swedish', 'Swedish'),
        ('Tachelhit', 'Tachelhit'),
        ('Tagalog', 'Tagalog'),
        ('Tajiki', 'Tajiki'),
        ('Tamil', 'Tamil'),
        ('Tatar', 'Tatar'),
        ('Telugu', 'Telugu'),
        ('Thai', 'Thai'),
        ('Tibetic Languages', 'Tibetic Languages'),
        ('Tigrigna', 'Tigrigna'),
        ('Tok Pisin', 'Tok Pisin'),
        ('Turkish', 'Turkish'),
        ('Turkmen', 'Turkmen'),
        ('Ukrainian', 'Ukrainian'),
        ('Urdu', 'Urdu'),
        ('Uyghur', 'Uyghur'),
        ('Uzbek', 'Uzbek'),
        ('Vietnamese', 'Vietnamese'),
        ('Warlpiri', 'Warlpiri'),
        ('Welsh', 'Welsh'),
        ('Wolof', 'Wolof'),
        ('Xhosa', 'Xhosa'),
        ('Yakut', 'Yakut'),
        ('Yiddish', 'Yiddish'),
        ('Yoruba', 'Yoruba'),
        ('Yucatec', 'Yucatec'),
        ('Zapotec', 'Zapotec'),
        ('Zulu', 'Zulu')
    ]

    name = models.CharField(choices=language_choices, max_length=100, unique=True)

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

    def __str__(self):
        return self.username


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    last_name = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    birthdate = models.DateTimeField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('main:myaccounts:my-account', kwargs={"id": self.id})




class Child(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, blank=True, default='')
    first_name = models.CharField(max_length=100, default='')
    birthdate = models.DateTimeField(null=True)
    native_language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1, related_name="native_language")
    hobbies = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    # language_to_learn = models.ManyToManyField(Language, default="")

    # date_joined = models.DateField(auto_now_add=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1, related_name="wish_language")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, default=0, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("main:mykids:child-view", kwargs={"id": self.id})

    def get_corresponent_url(self):

        return reverse("main:meeting-update", kwargs={"id": self.id})


class Languagetolearn(models.Model):
    child_correspondent = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='child_correspondent',
                                            default=10)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='child_participant')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1, related_name="participant_language")
    correspondent_language = models.ForeignKey(Language, default=1, on_delete=models.CASCADE,
                                               related_name='correspondent_language', blank=True)

    status_choice = [('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')]
    validation_status = models.CharField(max_length=10, choices=status_choice, default="Pending")
    link_video = models.CharField(max_length=500, blank=True, default='',)
    meeting_id = models.IntegerField(default=0)

    date_slot = models.DateField()
    start_time_slot = models.TimeField()
    end_time_slot = models.TimeField()

    def get_absolute_url(self):
        return reverse('main:mykids:event-detail', args=(self.id,))


    def __str__(self):
        self.meeting_id


"""

class Message(models.Model):
    message_to = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_to')
    message_from = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_from')
    message_date = models.DateTimeField('date sent', auto_now_add=True)
    content = models.TextField()

    # title = models.CharField(max_length=20)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    date_slot = models.DateField()
    start_time_slot = models.TimeField()
    end_time_slot = models.TimeField()

"""





class Message(models.Model):
    message_to = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_to')
    message_from = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='message_from')
    message_date = models.DateTimeField('date sent', auto_now_add=True)
    content = models.TextField(max_length=300)
    # title = models.CharField(max_length=20)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
