# Generated by Django 4.0.5 on 2022-08-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0017_nsapdata_faulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherdata',
            name='faulty',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
