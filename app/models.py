from turtle import mode
from django.db import models

# Create your models here.
class nsapdata(models.Model):
    aadhar_no = models.CharField(max_length=12)
    name= models.CharField(max_length=20)
    dob=models.DateField()
    pension_id=models.CharField(max_length=10)
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    income=models.CharField(max_length=20)
    disability=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    status= models.IntegerField()
    widow=models.CharField(max_length=3)
    bpl_family_id=models.CharField(max_length=10)
    EPIC_id=models.CharField(max_length=10)
    faulty = models.CharField(max_length=10, default='0')

class otherdata(models.Model):
    aadhar=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    income=models.CharField(max_length=20)
    Dob=models.DateField()
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    disability=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    status= models.IntegerField()
    widow=models.CharField(max_length=3)
    bpl_family_id=models.CharField(max_length=10)
    EPIC_id=models.CharField(max_length=10)
    faulty = models.CharField(max_length=10, default='0')



class emp(models.Model):
    emp_fname=models.CharField(max_length=30)
    emp_lname=models.CharField(max_length=30)
    emp_email=models.EmailField()
    emp_password=models.CharField(max_length=20)

class nopension(models.Model):
    aadhar=models.CharField(max_length=20,primary_key= True)
    Name=models.CharField(max_length=20)
    Dob=models.DateField()
    state=models.CharField(max_length=30)
    pincode=models.CharField(max_length=6)
    income=models.CharField(max_length=20)
    disability=models.CharField(max_length=3)
    gender=models.CharField(max_length=10)
    widow=models.CharField(max_length=3)
    bpl_family_id=models.CharField(max_length=10)
    EPIC_id=models.CharField(max_length=10)
    class Meta:
        managed=False
        db_table='nopension'



















        
