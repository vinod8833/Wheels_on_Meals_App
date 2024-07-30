import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.db.models.signals import post_save
from django.conf import settings
from app.models import Register
from django.contrib.auth.models import User 
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
# from .models import OrderItem

# from django.contrib.auth.models import User 
# from django.contrib.auth import login, update_session_auth_hash, authenticate
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.decorators import login_required
# from django.template.loader import render_to_string
# # Create your views here.

def Home_page(request):
    return render(request,"index.html")

def User_Dashboard(request):
    context ={}
    return render(request, "user_dashboard.html", context)

def Hotel_Dashboard(request):
    context ={}
    return render(request,"hotel_dashboard.html", context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def payment_view(request):
    return render(request, 'payment.html')


# def payment_details(request):
#     order_details = OrderItem.objects.all()
    
#     context = {
#         'order_details': order_details,
#     }
#     return render(request, 'payment_details.html', context)





def Registerr(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        username= request.POST['username']
        email= request.POST['email']
        phone= request.POST['phone']
        password= request.POST['password']
        gender= request.POST['gender']
        dob= request.POST['dob']
        address= request.POST['address']
        country= request.POST['country']
        state= request.POST['state']
        city= request.POST['city']
        reg = Register.objects.create(fullname=fullname,username=username,email=email,phone=phone,password=password,gender=gender,dob=dob,address=address,country=country,state=state,city=city)
        reg.save()
        context={'username': username}
        return render(request, "registration.html", context)
    return render(request, "registration.html")


def User_login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # emp =Register.objects.get(user=username)
            return redirect('user_dashboard')
        else:
            alert = True
            msg ="Username and password incorrect"
            return render(request,"user_login.html",{"alert":alert, "msg":msg})
    return render(request, "user_login.html")


def house_owner(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # emp =Register.objects.get(user=username)
            return redirect('Hotel_Dashboard')
        else:
            alert = True
            msg ="Username and password incorrect"
            return render(request,"hotel.html",{"alert":alert, "msg":msg})
    return render(request, "hotel.html")