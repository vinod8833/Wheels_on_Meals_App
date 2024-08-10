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
    GENDER_CHOICE= [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE,null=True)
    nationality = models.CharField(max_length=50,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    email_address = models.EmailField()
    street_address = models.CharField(max_length=255,null=True)
    # city = models.CharField(max_length=100)
    # state_province = models.CharField(max_length=100,null=True)
    # postal_code = models.CharField(max_length=20,null=True)
    # country = models.CharField(max_length=50,null=True)
    profile =models.ImageField(upload_to="", null=True,help_text="<br><b>upload profile photo<b>")
    username = models.CharField(max_length=50, unique=True,null=True)
    password = models.CharField(max_length=50,null=True)
    
    def str(self):
        return f"{self.username}"



class Item(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='', null=True, help_text="<br><b>upload profile photo<b>")


