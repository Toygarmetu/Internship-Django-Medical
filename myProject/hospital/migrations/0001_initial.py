# Generated by Django 5.0.1 on 2024-01-31 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.TextField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('dosage', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('illness', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ManyToManyField(to='hospital.specialization'),
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('severity', models.CharField(max_length=100)),
                ('commonness', models.CharField(max_length=100)),
                ('possible_treatment', models.CharField(max_length=100)),
                ('related_diseases', models.ManyToManyField(to='hospital.medicalcondition')),
            ],
        ),
        migrations.AddField(
            model_name='medicalcondition',
            name='symptoms',
            field=models.ManyToManyField(to='hospital.symptom'),
        ),
    ]
