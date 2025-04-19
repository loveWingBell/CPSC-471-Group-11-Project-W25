from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """ Common fields for all user profiles """
    healthcare_number = models.CharField(max_length=20, unique=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    insurance = models.CharField(max_length=50)
    
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
    
class Doctor(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
    
class LabTechnician(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    specialization = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)

    def __str__(self):
        return f"Lab Tech: {self.user.first_name} {self.user.last_name}"

class Pharmacist(UserProfile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # optional extra fields
    license_number = models.CharField(max_length=50)
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Pharmacist: {self.user.first_name} {self.user.last_name}"