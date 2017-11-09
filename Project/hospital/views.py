from django.shortcuts import render #imports a render method which is userd to load the template
from django.http import HttpResponse #Used to return the Http Response
from django.db import connection #Used to Connect with The Database
from django.contrib.auth.models import User #Used to store the login Information
from django.contrib.auth import authenticate, login, logout #authenticate is used to confirm the logging user details
import MySQLdb
from django.contrib.auth.decorators import login_required
import pickle

# Create your views here.


def home(request):
    '''
        Home page..
    '''
    return HttpResponse(render(request, "hospital/home.html"))



def login_user(request):
    '''
        Acccepts the Login Details And checks wether the user is authenticated
    '''
    if(request.method == "POST"):
        username = request.POST.get('un')
        password = request.POST.get('pwd')
        #Authenticating The User Details
        user = authenticate(username = username, password = password)

        if(user):
            login(request, user)
            # If Registered Then Proceed
            return HttpResponse(render(request, "hospital/login_success.html"))

        else:
            #if Not Registered Then ask to signup
            return HttpResponse(render(request, "hospital/login_fail.html"))
    else:
        #If the method is "GET"
        return HttpResponse(render(request, "hospital/login.html"))




def signup(request):
    '''
        SignUp Page Accepts the signup Details.....
    '''

    ob = open('hospital/test.p','rb')
    ID = pickle.load(ob)
    ID = float(ID)
    if(request.method == "POST"):
        ''' ID = int(request.POST.get('ID')) '''
        name = request.POST.get('Full_name')
        address = request.POST.get('Address')
        contact = int(request.POST.get('Contact'))
        gender = request.POST.get('Gender')
        password = request.POST.get('Password')
        Cpassword = request.POST.get('CPassword')
        ob.close()
        if(password!=Cpassword):
            return HttpResponse("Passwords Do not Match")

        try:
            #Inserting the values into User table(Builtin) Which is checked for User Authentication The None feild is for email
            user = User.objects.create_user(name, None, password)
            #Establish The Connection
            c = connection.cursor()
            #Executing The Query
            ID += 1
            c.execute("INSERT INTO hospital_signup(patient_id,Name,Address,Contact,Gender,Password) VALUES ('%d','%s', '%s', '%d', '%s', '%s')" % (ID, name, address, contact, gender, password))
            ob = open('hospital/test.p', 'wb')
            pickle.dump(ID, ob)
            ob.close()
            return HttpResponse(render(request, "hospital/signsuccess.html"))
        except Exception as e:
            print(e)

    else:
        #If the method is "GET"
        return HttpResponse(render(request, "hospital/signup.html"))


@login_required
def appointment(request):
    '''
        The Appointment page Creates an Appointment with the Doctor
    '''
    if(request.method=='POST'):
        pid = int(request.POST.get('pid'))
        Pname = request.POST.get('pname')
        docname = request.POST.get('docName')
        appointment_date = request.POST.get('date')
        appointment_time = request.POST.get('time')
        disease = request.POST.get('ill')
        age = request.POST.get('age')

        try:
            c = connection.cursor()
            c.execute("INSERT INTO hospital_appointment VALUES ('%d','%s', '%s', '%s', '%s', '%s', '%s')" % (
                pid, Pname, docname, appointment_date, appointment_time, disease, age))
            c.execute("Select * from hospital_appointment")
            appointments = c.fetchall()
            context = {"appointments" : appointments}
            return HttpResponse(render(request, "hospital/appointment_success.html", context))

        except Exception as e:
            print(e)
            
    else:
        #If the method is "GET"
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

