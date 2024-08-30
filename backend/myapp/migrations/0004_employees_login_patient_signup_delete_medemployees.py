# Generated by Django 5.1 on 2024-08-30 09:30

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_departments_medemployees_delete_meduser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeName', models.CharField(max_length=100)),
                ('DateEmployed', models.DateField()),
                ('Employees_Title', models.CharField(choices=[('DR', 'Doctor'), ('RN', 'Registered Nurse'), ('LT', 'Laboratory technician'), ('PH', 'Pharmacist'), ('CT', 'Consultant'), ('MD', 'Medical Director'), ('OB-GYN', 'Obstetrician and Gynaecologist'), ('Admin', 'Admin'), ('Recept', 'Receptionist'), ('CS', 'Clinical Staff'), ('OT', 'Other Staff')], default='DR', max_length=15)),
                ('Department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=10)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('medical_record_number', models.CharField(max_length=100, unique=True)),
                ('date_registered', models.DateTimeField(default=django.utils.timezone.now)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('blood_type', models.CharField(blank=True, max_length=10, null=True)),
                ('genotype', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MedEmployees',
        ),
    ]
