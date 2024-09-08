from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Departments(models.Model):
    """Department that the employees belong to"""
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.DepartmentName
    

class Employees(models.Model):
    """Employees that will have signup and login access
      to patient data and adding new records"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                related_name='employee_profile')
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = set_unusable_password()
    is_staff = True
    is_active = False
    last_login = DateTimeField
    Department = models.ForeignKey(
        Departments,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employee_profile'
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
        choices=EmployeesTitle.choices,
        default=EmployeesTitle.DOCTOR,
    )

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    def __str__(self):
        return self.EmployeeName


# Patient Portal User
class Patient(models.Model):
    """Patient Registration Form"""
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
    medical_record_number = models.IntegerField(primary_key=True, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    # Optional fields
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    blood_type = models.CharField(max_length=10, null=True, blank=True)
    genotype = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
class Signup(models.Model):
    """Signup for employees"""
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


class Medication(models.Model):
    """Medication class"""
    name = models.TextField(max_length=100)
    type = models.CharField(
        max_length=50,
        choices=[
            ('Brand', 'Brand Name'),
            ('Generic', 'Generic Name')
        ]
    )
    quantity_in_stock = models.IntegerField()

    def check_availability(self):
        """if self.quantity_in_stock != 0:
            self.name"""

    def reduce_stock(self):
        pass

    def __str__(self):
        return self.name

class Prescription(models.Model):
    """Prescription Class"""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_staff = models.ForeignKey(
        Employees,
        on_delete=models.SET_NULL,
        null=True
    )
    medications = models.ManyToManyField(Medication)
    dosage = models.IntegerField()

    def __str__(self):
        medications_list = ', '.join([med.name for med in self.medications.all()])
        return f"Patient: {self.patient}, Medications: {medications_list}, Dosage: {self.dosage}"

    def validate_prescription(self):
        pass

    def calculate_total_cost(self):
        pass


class StatusChoices(models.TextChoices):
    PENDING = 'PEN', _('pending')
    CONFIRMED = 'CON', _('confirmed')
    CANCELLED = 'CANCEL', _('cancelled')
    COMPLETED = 'COM', _('completed')


class Order(models.Model):
    """Med Order"""
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    status = models.CharField(
            max_length=10,
            choices=StatusChoices.choices,
            default=StatusChoices.PENDING,
    )
    order_date = models.DateTimeField(auto_now_add=True)
    total_cost = models.FloatField()

    def process_order(self):
        pass

    def update_status(self):
        pass


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        'Employees',
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={
            'title': [
                'DR',
                'CT',
            ]
        }
    )
    appointment_date = models.DateField()
    status = models.CharField(
            max_length=10,
            choices=StatusChoices.choices,
            default=StatusChoices.PENDING,
    )

    def schedule_appointment(self):
        pass

    def reshedule_appointment(self):
        pass

    def cancel_appointment(self):
        pass

    def completed_appointment(self):
        pass
