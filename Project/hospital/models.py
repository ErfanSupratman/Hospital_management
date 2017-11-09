from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class SignUp(models.Model):
    '''
        This creats a table By Name hospital_signup(hospital is the app name) in the Hospital Databse.Migrate to Make Changes Happen
    '''
    patient_id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 200)
    Contact = models.BigIntegerField()
    Gender = models.CharField(max_length = 8)
    Password = models.CharField(max_length = 20)


class Appointment(models.Model):
    '''
        This creats a table By Name hospital_appointment(hospital here is you App name) in the Hospital Database.Migrate to Make Changes Happen
    '''
    id = models.IntegerField(primary_key=True)
    Patient_Name = models.CharField(max_length = 20)
    Doctor_Name = models.CharField(max_length = 20)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField()
    Disease = models.CharField(max_length = 20)
    Age = models.IntegerField()
    
