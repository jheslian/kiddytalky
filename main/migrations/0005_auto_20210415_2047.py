# Generated by Django 3.1.7 on 2021-04-15 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210415_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date_slot',
        ),
        migrations.RemoveField(
            model_name='message',
            name='end_time_slot',
        ),
        migrations.RemoveField(
            model_name='message',
            name='language',
        ),
        migrations.RemoveField(
            model_name='message',
            name='start_time_slot',
        ),
    ]
