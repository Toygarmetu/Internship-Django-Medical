# Generated by Django 5.0.1 on 2024-02-09 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_alter_appointment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalcondition',
            name='symptoms',
        ),
    ]
