from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Departments(models.Model):
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.DepartmentName


class Employees(models.Model):
    EmployeeName = models.CharField(max_length=100)
    Department = models.ForeignKey(
        Departments,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    DateEmployed = models.DateField()

    class EmployeesTitle(models.TextChoices):
        DOCTOR = "DR", _("Doctor")
        REGISTERED_NURSE = "RN", _("Registered Nurse")
        LABORATORY_TECHNICIAN = "LT", _("Laboratory technician")
        PHARMACIST = "PH", _("Pharmacist")
        CONSULTANT = "CT", _("Consultant")
        MEDICAL_DIRECTOR = "MD", _("Medical Director")
        GYNAECOLOGIST = "OB-GYN", _("Obstetrician and Gynaecologist")
        ADMINISTRATOR = "Admin", _("Admin")
        RECEPTIONIST = "Recept", _("Receptionist")
        OTHER_CLINICAL_STAFF = "CS", _("Clinical Staff")
        OTHERS = "OT", _("Other Staff")
    Employees_Title = models.CharField(
        max_length=15,
        choices=EmployeesTitle,
        default=EmployeesTitle.DOCTOR,
    )

    def __str__(self):
        return self.EmployeeName


class Signup(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


""" class Login(models.Model):
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def account_exist(self):
        try:
            # Check if account exists
            user = Signup.objects.get(
                email=self.email,
                username=self.username
            )
            # Verify that the password is correct
            if check_password(self.password, user.password):
                return True
            else:
                return False
        except Signup.DoesNotExist:
            print(f"Acount {self.email} or {self.username} does not exist")
            return False"""


class Patient(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('F', 'Female'),
            ('M', 'Male'),
            ('O', 'Other')
        ]
    )
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    medical_record_number = models.CharField(max_length=100, unique=True)
    date_registered = models.DateTimeField(default=timezone.now)

    # Optional fields
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    blood_type = models.CharField(max_length=10, null=True, blank=True)
    genotype = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PatientFolder(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medicalhistory = models.TextField()

    def __str__(self):
        return self.name
