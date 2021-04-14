# Generated by Django 3.1.7 on 2021-04-13 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visio_start', models.DateTimeField()),
                ('visio_end', models.DateTimeField()),
                ('visio_date', models.DateTimeField()),
                ('link_video', models.CharField(blank=True, default='', max_length=500)),
                ('child_correspondent', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='child_correspondent', to='main.child')),
                ('child_participant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='child_participant', to='main.child')),
                ('correspondent_language', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='correspondent_language', to='main.language')),
                ('participant_language', models.ForeignKey(default='English', on_delete=django.db.models.deletion.CASCADE, related_name='participant_language', to='main.language')),
            ],
        ),
    ]
