from django.db import models

# Create your models here.

class SignUp(models.Model):
    '''
        This creats a table Name Signup(or hospital_signup i.e preceeding with your databaseName) Migrate to Make Changes Happen
    '''
    patient_id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 200)
    Contact = models.BigIntegerField()
    Gender = models.CharField(max_length = 8)
    Category = models.CharField(max_length = 20)

