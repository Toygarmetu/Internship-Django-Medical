# Generated by Django 5.0.1 on 2024-02-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
