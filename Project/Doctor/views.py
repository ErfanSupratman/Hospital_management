from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import SignUp
# Create your views here.

def Doctor_SignUp(request):
    if(request.method == "POST"):
        dname = request.POST.get('Full_name')
        address = request.POST.get('Address')
        contact = int(request.POST.get('Contact'))
        special = request.POST.get('special')
        degree = request.POST.get('degree')
        gender = request.POST.get('Gender')
        pemail = request.POST.get('email')
        dpassword = request.POST.get('Password')
        Cpassword = request.POST.get('CPassword')
        dnames = dname.split()
        Id = SignUp.objects.count()
        Id+=10000

        if(dpassword != Cpassword):
            context = {"stop": True}
            return HttpResponse(render(request, "Doctor/signup.html", context))
        name = "Dr "+dname
        try:
            user = User.objects.create_user(username=name, password=dpassword, email=pemail, first_name=dnames[0], last_name=dnames[-1], id=Id, is_staff=1)
            c = connection.cursor()
            c.execute("Insert into Doctor_signup values(%d,'%s','%s',%d,'%s','%s','%s','%s','%s')" % (Id,name,address,contact,pemail,special,degree,gender,dpassword))
            return HttpResponse(render(request, "Doctor/signsuccess.html"))
        except Exception as e:
            print(e)
    else:
        return HttpResponse(render(request, 'Doctor/signup.html'))

def Doctor_login(request):
    if(request.method == 'POST'):
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        user = authenticate(username = un, password = pwd)
        if(user):
            login(request, user)
            name = str(user.username)
            c = connection.cursor()
            c.execute(
                "Select * from hospital_appointment where Doctor_Name='%s'" % (un))
            out = c.fetchall()
            context = {'list' : out}
            return HttpResponse(render(request, 'Doctor/login_success.html', context))
        else:
            return HttpResponse("Not Authenticated")
    else:
        return HttpResponse(render(request, 'Doctor/login.html'))


