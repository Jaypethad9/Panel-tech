from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from web.models import Report,product
from datetime import datetime

from .models import product
def home(request):
    pros= product.objects.all()
    return render(request,'home.html',{'pros':pros})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.success(request, 'Invalid credentials')
            return redirect("login")
    else:
        return render(request,"ht.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username is already taken')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email is already taken')
            else:
                user = User.objects.create_user(email=email,username=username,password=password1)
                user.save()
                messages.success(request, 'Registration done')
                return redirect("login")
        else:
            messages.success(request, 'Password and confirm password is not matching')
    return render(request,"ht copy.html")

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out')
    return redirect("home")

def about(request):
    return render(request,"about.html")

def search(request):
    query = request.GET['query']
    all = product.objects.filter(name__icontains=query)
    params = {'all':all}
    return render(request,"search.html",params)

def contact(request):
    if request.method == "POST":
        name_us = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc_us = request.POST.get('desc')
        report = Report(name_us=name_us,email=email,phone=phone,desc_us=desc_us,date= datetime.today())
        report.save()
        messages.success(request, 'Your message has been sent')
    else:
        pros = product.objects.all()
        return render(request,"contact.html",{'pros':pros})
    pros = product.objects.all()
    return render(request,"contact.html",{'pros':pros})
    