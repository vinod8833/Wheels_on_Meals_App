# app/forms.py
from django import forms

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')], widget=forms.RadioSelect, required=True)
    dob = forms.DateField(label='Date of Birth', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age', required=True)
    phone = forms.CharField(label='Phone Number', required=True, widget=forms.TextInput(attrs={'type': 'tel'}))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'rows': 3}), required=True)
    country = forms.ChoiceField(label='Country', choices=[
        ('India', 'India'), ('USA', 'USA'), ('UK', 'UK'), ('Canada', 'Canada'), ('Australia', 'Australia'),
        ('Germany', 'Germany'), ('France', 'France'), ('Japan', 'Japan')
    ], required=True)
    state = forms.ChoiceField(label='State', choices=[
        ('Tamil Nadu', 'Tamil Nadu'), ('California', 'California'), ('Andhra Pradesh', 'Andhra Pradesh'), 
        ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), 
        ('Goa', 'Goa'), ('Gujarat', 'Gujarat')
    ], required=True)
    city = forms.ChoiceField(label='City', choices=[
        ('Coimbatore', 'Coimbatore'), ('Bengaluru', 'Bengaluru'), ('Mumbai', 'Mumbai'), 
        ('Jaipur', 'Jaipur'), ('Lucknow', 'Lucknow'), ('Hyderabad', 'Hyderabad')
    ], required=True)



# Email configuration
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    
    




    
    
    
    
    
