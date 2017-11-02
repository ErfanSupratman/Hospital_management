from django.db import models

# Create your models here.

class SignUp(models.Model):
    '''
        This creats a table By Name hospital_signup in the Hospital Databse.Migrate to Make Changes Happen
    '''
    patient_id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 200)
    Contact = models.BigIntegerField()
    Gender = models.CharField(max_length = 8)
    Category = models.CharField(max_length = 20)

class Appointment(models.Model):
    '''
        This creats a table By Name hospital_appointment in the Hospital Database.Migrate to Make Changes Happen
    '''
    Patient_Name = models.CharField(max_length = 20)
    Doctor_Name = models.CharField(max_length = 20)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField()
    Disease = models.CharField(max_length = 20)
    Lastvisited = models.DateField()
    Age = models.IntegerField()
    