# Generated by Django 5.1.1 on 2024-09-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_content_note_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
