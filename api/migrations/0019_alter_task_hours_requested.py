# Generated by Django 5.1.1 on 2024-09-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='hours_requested',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
