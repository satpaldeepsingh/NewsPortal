from django.shortcuts import render ,HttpResponse , redirect 
from  NewsApp.models import User 
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required



def HomeView(request):
    print("HRER")
    return render(request ,"home.html")

def create_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        show = make_password(password)
        query = User.objects.create(name = name , email = email , password = show)
        query.save()
        return render(request ,'login.html')
    return render(request,'signup.html') 


def Log_In(request):
    if request.method == "POST":
        uname = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return HttpResponse("login failed")
    else:
        return render(request,"login1.html")    


@login_required
def index(request):
    return render(request,"index.html")


@login_required
def AddNews(request):
    return render(request,"dashboard.html")

def Logout(request):
    logout(request)
    return HttpResponse("Logged out sucessfully")
