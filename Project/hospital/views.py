from django.shortcuts import render #imports a render method which is userd to load the template
from django.http import HttpResponse #Used to return the Http Response
from django.db import connection #Used to Connect with The Database
from django.contrib.auth.models import User #Used to store the login Information
from django.contrib.auth import authenticate, login, logout #authenticate is used to confirm the logging user details
import MySQLdb

# Create your views here.


def home(request):
    '''
        Home page..
    '''
    return HttpResponse(render(request, "hospital/home.html"))



def login(request):
    '''
        Acccepts the Login Details And checks wether the user is authenticated
    '''
    if(request.method == "POST"):
        username = request.POST.get('un')
        password = request.POST.get('pwd')
        #Authenticating The User Details
        user = authenticate(username = username, password = password)

        if(user):
            #login(request, user)
            # If Registered Then Proceed
            return HttpResponse("Login Successful Enjoy....!!!")

        else:
            #if Not Registered Then ask to signup
            return HttpResponse(render(request, "hospital/login_fail.html"))
    else:
        return HttpResponse(render(request, "hospital/login.html"))




def signup(request):
    '''
        SignUp Page Accepts the signup Details.....
    '''
    if(request.method == "POST"):
        ID = int(request.POST.get('ID'))
        name = request.POST.get('Full_name')
        address = request.POST.get('Address')
        contact = int(request.POST.get('Contact'))
        gender = request.POST.get('Gender')
        category = request.POST.get('Category')
        password = request.POST.get('Password')
        Cpassword = request.POST.get('CPassword')
        if(password!=Cpassword):
            return HttpResponse("Passwords Do not Match")

        try:
            #Inserting the values into User table(Builtin) Which is checked for User Authentication The None feild is for email
            user = User.objects.create_user(name, None, password)
            #Establish The Connection
            c = connection.cursor()
            #Executing The Query
            c.execute("INSERT INTO hospital_signup VALUES ('%d', '%s', '%s', '%d', '%s', '%s')" % (ID, name, address, contact, gender, category))
            return HttpResponse(render(request, "hospital/signsuccess.html"))
        except Exception as e:
            print(e)

    else:
        return HttpResponse(render(request, "hospital/signup.html"))



def appointment(request):
    '''
        The Appointment page Creates an Appointment with the Doctor
    '''
    if(request.method=='POST'):
        return HttpResponse("<h1>Details got inserted in the table</h1>")
    else:
        return HttpResponse(render(request, "hospital/appointment.html"))



def forgetpassword(request):
    '''
        Gives the link to password reset if Forgot....
    '''
    return HttpResponse(render(request, "hospital/forgetpassword.html"))



def signsuccess(request):
    '''
        Used to Redirect To the Login Page
    '''
    return HttpResponse(render(request, "hospital/signsuccess.html")) 

