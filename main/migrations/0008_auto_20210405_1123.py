# Generated by Django 3.1.7 on 2021-04-05 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210405_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='country',
            field=models.CharField(default='USA', max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]