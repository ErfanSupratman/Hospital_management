from django.db import models

# Create your models here.
class SignUp(models.Model):
    '''
        This creats a table By Name Doctor_signup(hospital is the app name) in the Hospital Databse.Migrate to Make Changes Happen
    '''
    Doctor_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)
    Contact = models.BigIntegerField()
    Email = models.CharField(max_length=30)
    Specialization = models.CharField(max_length=30)
    Degree = models.CharField(max_length=10)
    Gender = models.CharField(max_length=8)
    Password = models.CharField(max_length=20)


