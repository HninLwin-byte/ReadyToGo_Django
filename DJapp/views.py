
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.contrib import messages 
from .models import feature, image, restaurant
# Create your views here.

def index(request):
    features = feature.objects.all()
   

    return render(request,"index.html", {'features':features})

'''def register(request):
    if request.method == "POST":
       
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']
        Password2 = request.POST['password2']
        print(Username)
    
        if Password == Password2:
            if User.objects.filter(email= Email).exists():
                messages.info(request, "Email is already used")
                return redirect("register")
            elif User.objects.filter(username = Username).exists():
                messages.info(request, "Username already used")
                return redirect('register')
            else:
                user = User.objects.creat_user(username=Username, email=Email, password=Password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password is incorrect")
            return redirect('register')


    else:
        return render(request, 'register.html')'''

'''def login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential Ivalid')
            return redirect('login')
    else:
     return render(request, "login.html")

def post(request,p):
    return render(request, "post.html", {'pg': p})'''


'''def counter(request):
    text = request.POST['text']
    amoun_of_text = len(text.split())
    return render(request,"counter.html", {'amount':amoun_of_text} )'''

def services(request):
    features = feature.objects.all()
    return render(request,"services.html", {'features':features})

def pricing(request):
    return render(request,"pricing.html")

def portfolio(request):
    return render(request,"portfolio.html")

def restaurants(request):
    features = feature.objects.all()
   
    return render(request,"restaurants.html", {'features':features})
    

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")



