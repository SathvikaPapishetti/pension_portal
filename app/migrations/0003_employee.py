# Generated by Django 4.0.5 on 2022-08-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0002_alter_nsapdb_age_alter_otherdb_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_password', models.CharField(max_length=20)),
            ],
        ),
    ]
