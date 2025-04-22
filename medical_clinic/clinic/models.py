from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class UserProfile(models.Model):
    """ Common fields for all user profiles """
    healthcare_number = models.CharField(max_length=20, unique=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    insurance = models.CharField(max_length=50, blank=True)
    
    # optional extra fields
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    
    class Meta:
        abstract = True

class Patient(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    emergency_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Patient: {self.user.first_name} {self.user.last_name}"
    
    def get_absolute_url(self):
        return reverse("patient-list")
    
class Doctor(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    specialty = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
    
class LabTechnician(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    specialization = models.CharField(max_length=100, blank=True)
    certification = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Lab Tech: {self.user.first_name} {self.user.last_name}"

class Pharmacist(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    license_number = models.CharField(max_length=50, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"Pharmacist: {self.user.first_name} {self.user.last_name}"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    appointment_datetime = models.DateTimeField(default=timezone.now)
    reason_for_visit = models.CharField(max_length=255, blank=True)
    observations = models.TextField(blank=True)
    
    def __str__(self):
        return f"Appointment: {self.patient.user.first_name} with Dr.{self.doctor.user.last_name} on {self.appointment_datetime.strftime('%Y-%m-%d %H:%M')}"
    
    # def get_absolute_url(self):
    #     return reverse("appointment-list")
    
class Medical_Condition(models.Model):
    condition_name = models.CharField(max_length=30)
    condition_description = models.TextField(blank=True)

    def __str__(self):
        return f"Condition: {self.condition_name}\nDescription: {self.condition_description if self.condition_description else "No description"}"

class Diagnose(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    condition = models.ForeignKey(Medical_Condition, on_delete=models.CASCADE)
    status_now = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("diagnose-list")

    def __str__(self):
        return f"{self.appointment.patient.user.first_name} was diagnosed with {self.condition.condition_name} by Dr.{self.appointment.doctor.user.last_name} on {self.appointment.appointment_datetime.strftime('%Y-%m-%d %H:%M')}\nCurrent Status:{"Still  possess" if self.status_now else "No longer possess"}"
    
class Sample(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sample_type = models.CharField(max_length=5, choices=[('U', 'Urine'), ('B', 'Blood')])
    obtained_date = models.DateTimeField(default=timezone.now)
    technician = models.ForeignKey(LabTechnician, on_delete=models.SET_NULL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("sample-list")

    def __str__(self):
        return f"This {self.sample_type} sample came from {self.patient.user.first_name} on {self.obtained_date.strftime('%Y-%m-%d %H:%M')}. {f"Tested by {self.techician.user.first_name}." if self.technician else "The sample has not been tested yet."}"
    
class Pill(models.Model):
    pill_name = models.CharField(max_length=30)
    pill_description = models.TextField(blank=True)

    def __str__(self):
        return f"Condition: {self.pill_name}\nDescription: {self.pill_description if self.pill_description else "No description"}"

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.SET_NULL, blank=True, null=True)
    pill_count = models.PositiveSmallIntegerField(default=7)
    pill_refills = models.PositiveSmallIntegerField(default=0)
    concentration = models.PositiveSmallIntegerField(default=20)
    instructions = models.TextField(blank=True)
    created = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("prescription-list")

    def __str__(self):
        return f"This prescription for {self.appointment.patient.user.first_name} was written by Dr.{self.appointment.patient.user.last_name}.\nPill: {self.pill.pill_name}, Count: {self.pill_count}, Refills: {self.pill_refills}, Concentration: {self.concentration} mg\n{f"Instructions: {self.instructions}\n" if self.instructions else ""}{f"Prescription taken by {self.pharmacist.user.first_name} on {self.created.strftime('%Y-%m-%d')}" if self.pharmacist else "This prescription has not been taken by a pharmacist yet."}"



