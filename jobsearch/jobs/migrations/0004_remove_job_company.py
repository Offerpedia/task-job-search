# Generated by Django 5.1 on 2024-09-01 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_application_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
    ]
