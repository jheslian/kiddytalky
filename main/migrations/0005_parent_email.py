# Generated by Django 3.1.7 on 2021-04-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210409_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
