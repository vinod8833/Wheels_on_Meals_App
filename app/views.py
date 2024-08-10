import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from app.models import Register, FoodAppOwner, Item

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.html"
                    context = {
                        "email": user.email,
                        "domain": get_current_site(request).domain,
                        "site_name": "Your Site Name",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": request.scheme,
                    }
                    email_message = render_to_string(email_template_name, context)
                    try:
                        email = EmailMessage(subject, email_message, to=[user.email])
                        email.send()
                    except:
                        return render(request, 'password_reset_form.html', {'form': form, 'error': 'Failed to send email.'})
                return redirect("password_reset_done")
            else:
                return render(request, 'password_reset_form.html', {'form': form, 'error': 'No users found with this email address.'})
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})

def password_reset_confirm(request, uidb64=None, token=None):
    user = get_user(uidb64)
    if request.method == 'POST':
        form = SetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_reset_complete')
    else:
        form = SetPasswordForm(user=user)
    return render(request, 'password_reset_confirm.html', {'form': form})

def get_user(uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    return user

def Home_page(request):
    return render(request, "index.html")

def User_Dashboard(request):
    context = {}
    return render(request, "user_dashboard.html", context)

def Hotel_Dashboard(request):
    context = {}
    return render(request, "hotel_dashboard.html", context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def Payment(request):
    return render(request, 'payment.html')

def Prof(request):
    user = request.user
    mspro = FoodAppOwner.objects.get(user=user)
    context = {'mspro': mspro}
    return render(request, 'profile.html', context)

def Order(request):
    return render(request, 'user_order_status.html')

def Hotel(request):
    return render(request, 'hotel_details.html')

def User(request):
    return render(request, 'user_details.html')

def Log(request):
    return render(request, 'logout.html')

def Pro(request):
    return render(request, "profile.html")

def Orders(request):
    return render(request, "user_orders.html")

def Return(request):
    return render(request, "return_policy.html")

def Out(request):
    return render(request, "user_logout.html")

def contact_view(request):
    return render(request, 'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send email
        subject = 'New Contact Form Submission'
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['recipient@example.com']  # Replace with your email address

        send_mail(subject, message_body, from_email, recipient_list)

        return redirect('thank_you')

    return render(request, 'contact.html')

def thank_you(request):
    return render(request, 'thank_you.html')

def Registerr(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        gender = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        reg = Register.objects.create(fullname=fullname, username=username, email=email, phone=phone, password=password, gender=gender, dob=dob, address=address, country=country, state=state, city=city)
        reg.save()
        context = {'username': username}
        return render(request, "registration.html", context)
    return render(request, "registration.html")

def User_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('User_Dashboard')
        else:
            alert = True
            msg = "Username and password incorrect"
            return render(request, "user_login.html", {"alert": alert, "msg": msg})
    return render(request, "user_login.html")

def Hotel_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                emp = FoodAppOwner.objects.get(user=user)
                login(request, user)
                return redirect('Hotel_Dashboard')  # Redirect to the owner's dashboard or a relevant page
            except ObjectDoesNotExist:
                alert = True
                msg = "User is not associated with a house owner profile"
                return render(request, "hotel.html", {"alert": alert, "msg": msg})
        else:
            alert = True
            msg = "Username and password incorrect"
            return render(request, "hotel.html", {"alert": alert, "msg": msg})
    return render(request, "hotel.html")

def Add_items(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.POST['image']
        add = Item.objects.create(item_name=item_name, description=description, price=price, image=image)
        add.save()
        context = {'item_name': item_name}
        return render(request, "add_items.html", context)
    return render(request, "add_items.html")
