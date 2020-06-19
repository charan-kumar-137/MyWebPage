import django.contrib.auth as djauth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from . import models


# Create your views here.

def index(request):  # renders respective page
    return render(request, 'index.html')


def login(request):  # renders respective page
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in')
        return redirect('home')
    return render(request, 'html/login.html')


@login_required(login_url='login')
def home(request):  # renders respective page but only if user is logged in or redirect to login_url
    return render(request, 'html/home.html')


def signup(request):  # renders respective page
    return render(request, 'html/signup.html')


def logout(request):  # renders respective page
    if request.user.is_authenticated:  # if user is logged in , show respective messages
        djauth.logout(request)
        messages.success(request, "Logout Successful")
        return render(request, 'index.html')
    messages.error(request, 'Logout Failed')
    return render(request, 'index.html')

def registration(request):
    return render(request,'html/registration.html')


def handle_signup(request):  # manage form input while signup
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Password not matching")
            return redirect('signup')

        # create user
        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.first_name = name
        my_user.save()

        # show respective messages for signup fail or success
        messages.success(request, 'Sign up Success')
        return render(request, 'index.html')

    else:
        messages.error(request, "Sign up Failed")
        return redirect('signup')


def handle_login(request):  # manage the input while login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user and display respective messages
        my_user = djauth.authenticate(request, username=username, password=password)
        if my_user is not None:
            djauth.login(request, my_user)
            messages.success(request, "Login Success")
            return redirect('home')

        else:
            messages.error(request, "Login Failed")
            return redirect('login')

    messages.error(request, 'Login Failed')
    return redirect('index')

def handle_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')
        description = request.POST.get('description','')

        register = models.Registration(name=name,email=email,phone=phone,city=city,
                                       state=state,zip=zip,description=description)
        register.save()
        messages.success(request,'Registration Success')
        return render(request,'html/registration.html')

    messages.error(request,'Registration Failed')
    return render(request,'html/registration.html')
