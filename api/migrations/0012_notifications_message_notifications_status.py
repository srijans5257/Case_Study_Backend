# Generated by Django 5.1.1 on 2024-09-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='message',
            field=models.CharField(default='xyz', max_length=255),
        ),
        migrations.AddField(
            model_name='notifications',
            name='status',
            field=models.CharField(choices=[('Read', 'Read'), ('Unread', 'Unread')], default='Read', max_length=10),
        ),
    ]
