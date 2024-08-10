from django.urls import path
from app import views
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import password_reset_request, password_reset_confirm  # Import your views here






 
urlpatterns = [
    path('',views.Home_page, name="home"),
    path('register', views.Registerr, name="user_register"),      
    path('user_login', views.User_login, name="User_login"),
    path('user_dashboard',views.User_Dashboard, name="User_Dashboard"),
    path('owner_login', views.Hotel_login, name="Hotel_login"),
    path('hotelier_dashboard', views.Hotel_Dashboard, name="Hotel_Dashboard"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),    
    path('admin_login/', views.admin_login, name='admin_login'),    
    path('payment/', views.Payment, name='Payment'),
    
    path('profile',views.Prof, name='Prof'),
    path('items', views.Add_items, name="Add_items"),
    path('order',views.Order, name="Order"),
    path('hotel', views.Hotel, name="Hotel"),
    path('user', views.User, name="User"),
    path('logout', views.Log, name="Log"),
    path('profile', views.Pro, name="Pro"),
    path('orders', views.Orders, name="Orders"),
    path('return',views.Return, name="Return"),
    path('logout',views.Out, name="Out"),
    path('contact/', views.contact_view, name='contact'),
    path('contact/submit/', views.submit_contact, name='submit_contact'),
    path('thank-you/', views.thank_you, name='thank_you'),

    
    
    path('password_reset/', password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm')
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    

 
 

