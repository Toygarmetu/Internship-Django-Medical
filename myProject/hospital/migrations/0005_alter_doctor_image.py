# Generated by Django 5.0.1 on 2024-02-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default='default_doctor.jpg', upload_to='images/'),
        ),
    ]