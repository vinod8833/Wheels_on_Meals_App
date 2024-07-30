from django.db import models
from django.contrib.auth.models import User
from datetime import date, timezone

# Create your models here.
class Register(models.Model):
    gen = [
        ('Male','male'),
        ('Female','female'),
    ]
    city = [
        ('India','india'),
        ('USA','SA'),
        ('UK','uK'),
        ('Canada','canada'),
        ('Australia','australia'),
        ('Germany','germany'),
        ('France','france'),
        ('Japan','japan'),
    ]
    exp = [
        ('Tamil Nadu','tamil nadu'),
        ('California','california'),
        ('Andhra Pradesh','andhra pradesh'),
        ('Arunachal Pradesh','arunachal pradesh'),
        ('Assam','Assam'),        
        ('Bihar','bihar'),       
        ('Chhattisgarh','chhattisgarh'),
        ('Goa','goa'),
        ('Gujarat','gujarat'),
    ]
    count =[
        ('Coimbatore','coimbatore'),
        ('Bengaluru','bengaluru'),
        ('Mumbai','mumbai'),
        ('Jaipur','jaipur'),        
        ('Lucknow','lucknow'),
        ('Hyderabad','hyderabad'),
    ]
    
    fullname = models.CharField(max_length=20,null=True)
    username = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, choices=gen, null=True)
    dob = models.DateField(null=True)
    age = models.IntegerField(max_length=10, null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=20,choices=city, null=True)
    state = models.CharField(max_length=20,choices=exp,null=True)
    city = models.CharField(max_length=20,choices=count,null=True)
    
    
    def __str__(self):
        return f"{self.username}"
    
    
    

class FoodAppOwner(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email_address = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, help_text="<br><b>Upload a profile photo</b>")
    
    # Restaurant Information
    restaurant_name = models.CharField(max_length=100, unique=True)
    restaurant_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=50)
    restaurant_description = models.TextField(null=True, blank=True)
    
    # Additional Information
    website = models.URLField(null=True, blank=True)
    social_media_links = models.JSONField(null=True, blank=True, help_text="Enter social media links as a JSON object")
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    operational_hours = models.CharField(max_length=100, null=True, blank=True)
    specialties = models.CharField(max_length=255, null=True, blank=True, help_text="E.g., Italian, Chinese, etc.")

    # Authentication
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Using a larger max_length for password storage

    def __str__(self):
        return self.restaurant_name


class OrderItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name