# Generated by Django 5.1.1 on 2024-10-01 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_profile_email_profile_firstname_profile_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
