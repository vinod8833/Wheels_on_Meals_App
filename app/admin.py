from django.contrib import admin
from app.models import FoodAppOwner
from django.core.mail import send_mail
from django.conf import settings

# Register your models here.
class YourModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model (request, obj, form, change)
        subject = "Regarding Employer ID and Password"
        message = "Hello" + obj.full_name + "!!\n" + "Your username: " + obj.username + "\n" + "Your Password:" + obj.password
        from_email = settings.EMAIL_HOST_USER
        to_email = obj.email_address
        send_mail(subject, message, from_email, [to_email])
admin.site.register(FoodAppOwner, YourModelAdmin)