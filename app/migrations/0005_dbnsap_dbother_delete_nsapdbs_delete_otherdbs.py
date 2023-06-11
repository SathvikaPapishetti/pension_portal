# Generated by Django 4.0.5 on 2022-08-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0004_nsapdbs_otherdbs_delete_nsapdb_delete_otherdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='dbnsap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('pension_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='dbother',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='nsapdbs',
        ),
        migrations.DeleteModel(
            name='otherdbs',
        ),
    ]
