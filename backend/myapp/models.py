from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os


# Create your models here.
"""Measurement class for weight, height, blood pressure etc"""
KG = 'Kg',
LBS = 'lbs',
Weight_units = [
    ('KG', 'Kilogramme'),
    ('LBS', 'Pounds'),
]
M = 'm',
CM = 'cm',
FT = 'ft',
Height_units = [
    ('M', 'Metre'),
    ('CM', 'Centimetre'),
    ('FT', 'Feet'),
]
Blood_pressure_units = 'mmHg'
POSITIVE = '+',
NEGATIVE = '-',
Blood_sign = [
    ('POSITIVE', 'positive'),
    ('NEGATIVE', 'negative'),
]


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
    EmployeeName = models.CharField(max_length=100)
    is_staff = True
    is_active = False
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
    username = models.CharField(max_length=191, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    profile_picture = models.ImageField(null=True, blank=True)
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
    patient_id = models.AutoField(primary_key=True, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    # Optional fields
    weight = models.FloatField(null=True, blank=True)
    weight_unit = models.CharField(max_length=10, choices=Weight_units, default='Kg')
    height = models.FloatField(null=True, blank=True)
    height_unit = models.CharField(max_length=10, choices=Height_units, default='cm')
    blood_type = models.CharField(max_length=10, null=True, blank=True)
    blood_sign = models.CharField(max_length=10, choices=Blood_sign, default='+')
    genotype = models.CharField(max_length=10, null=True, blank=True)
    folder = models.CharField(max_length=255, editable=False, null=True)

    def save(self, *args, **kwargs):
        """Overide save to create patient folder if not exists"""
        if not self.folder:
            self.folder = self.create_patient_folder()

        super(Patient, self).save(*args, **kwargs)

    def create_patient_folder(self):
        """Creating Patient Folder"""
        folder_path = os.path.join('patient', str(self.patient_id))

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def add_observation(self, SOAP):
        """Creating Soap Notes/Observations"""
        observation_file = os.path.join(self.folder, 'SOAP.txt')
        with open(observation_file, 'a') as file:
            timestamp = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            file.write(f"SOAP: {SOAP} - {timestamp}\n")

    def add_history(self, history):
        """Patient History"""
        history_file = os.path.join(self.folder, 'patientHistory.txt')
        with open(history_file, 'a') as file:
            timestamp = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            file.write(f"History: {history} - {timestamp}\n")

    def list_patient_folder(patient_id):
        folder_path = os.path.join('patients', str(patient_id))
        if default_storage.exists(folder_path):
            files = default_storage.listdir(folder_path)[1]
            return files
        return []

    def __str__(self):
        return f"(ID: {self.patient_id}) {self.first_name} {self.last_name}"


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
    price = models.FloatField()

    def reduce_stock(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity
            self.save()
            return True
        return False

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
        medications_list = ', '.join(
            [med.name for med in self.medications.all()]
            )
        return f"Patient: {self.patient}, Medications: {medications_list},\
        Dosage: {self.dosage}"

    def validate_prescription(self):
        if self.dosage <= 0:
            raise ValueError("Invalid dosage")
        if not self.medications.exists:
            """Check that the prescription contains meds"""
            raise ValueError("Enter at least one medication")

    def get_medication_quantity_ordered(self, medication):
        """Quantity of each medication prescribed"""
        try:
            prescription_medication = PrescriptionMedication.objects.get(
                prescription=self,
                medication=medication
            )
            return prescription_medication.quantity
        except PrescriptionMedication.DoesNotExist:
            return 0


class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('prescription', 'medication')


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

    def check_availability(self):
        unavailable_medications = []
        for medication in self.prescription.medications.all():
            if medication.quantity_in_stock <= 0:
                unavailable_medications.append(medication.name)

        if unavailable_medications:
            return f"The following medication(s) are not in stock:\
                {', '.join(unavailable_medications)}"
        return f"{medication.name} for {self.prescription} is available"

    def calculate_total_cost(self):
        total_cost = 0
        for medication in self.prescription.medications.all():
            quantity = self.prescription.get_medication_quantity_ordered(medication)
            total_cost += medication.price * quantity
        self.total_cost = total_cost
        self.save()
        return total_cost

    def process_order(self):
        availability_status = self.check_availability()
        if "not in stock" in availability_status:
            raise ValueError(availability_status)

        for medication in self.prescription.medications.all():
            quantity = self.prescription.get_medication_quantity_ordered(medication)
            if medication.reduce_stock(quantity):
                # Handle successful reduction
                pass
            else:
                # Handle failure
                pass

        self.update_status

    def update_status(self):
        if "not in stock" in self.check_availability():
            self.status = StatusChoices.CANCELLED
        else:
            self.status = StatusChoices.CONFIRMED
        self.save()


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
        if self.status != StatusChoices.PENDING:
            raise ValueError("Appointment cannot be scheduled!")

        if Appointment.objects.filter(doctor=self.doctor, appointment_date=self.appointment_date).exists():
            raise ValueError("Doctor is already booked for this date.")

        self.status = StatusChoices.CONFIRMED
        self.save()

    def reshedule_appointment(self, new_date):
        if Appointment.objects.filter(doctor=self.doctor, appointment_date=new_date).exists():
            raise ValueError("Doctor is already booked for this date")

        self.appointment_date = new_date
        self.status = StatusChoices.PENDING
        self.save()

    def cancel_appointment(self):
        if self.status == StatusChoices.COMPLETED:
            raise ValueError("Completed appointments cannot be canceled")

        self.status = StatusChoices.CANCELLED
        self.save()

    def completed_appointment(self):
        if self.status != StatusChoices.CONFIRMED:
            raise ValueError("Only confirmed appointments can be marked as completed")
        self.status = StatusChoices.COMPLETED
        self.save()
