# Generated by Django 3.1.7 on 2021-04-15 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_date', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('content', models.TextField()),
                ('date_slot', models.DateField()),
                ('start_time_slot', models.TimeField()),
                ('end_time_slot', models.TimeField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.child')),
                ('language', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.language')),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to='main.parent')),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to='main.parent')),
            ],
        ),
    ]