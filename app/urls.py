from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('',views.Home_page, name="home"),
    path('register', views.Registerr, name="user_register"),      
    path('user_login', views.User_login, name="User_login"),
    path('dashboard',views.User_Dashboard, name="User_Dashboard"),
    path('owner_login', views.house_owner, name="house_owner"),
    path('dashboard', views.Hotel_Dashboard, name="Hotel_Dashboard"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),    
    path('admin_login/', views.admin_login, name='admin_login'),    
    path('payment/', views.payment_view, name='payment'),
    
    # path('payment-details/', views.payment_details, name='payment_details')

    

 ]
 