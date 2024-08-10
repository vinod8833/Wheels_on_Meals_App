# Generated by Django 5.0.7 on 2024-08-01 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_foodappowner_alter_register_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodappowner',
            name='city',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='country',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='operational_hours',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='restaurant_address',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='restaurant_description',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='restaurant_name',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='social_media_links',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='specialties',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='foodappowner',
            name='website',
        ),
        migrations.AddField(
            model_name='foodappowner',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
