# Generated by Django 4.0.5 on 2022-08-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sih_app', '0012_alter_emp_emp_mname'),
    ]

    operations = [
        migrations.CreateModel(
            name='dbs_nsap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_no', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('pension_id', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('income', models.CharField(max_length=20)),
                ('disability', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('widow', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='dbs_other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=6)),
                ('disability', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('status', models.IntegerField()),
                ('widow', models.CharField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='db_nsaps',
        ),
        migrations.DeleteModel(
            name='db_others',
        ),
    ]
