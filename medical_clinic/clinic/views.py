from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient, Appointment, Doctor, Pharmacist, LabTechnician
from django.views.generic import CreateView
from .forms import PatientForm

def home(request):
    return render(request, 'home.html', {})

def doctor_dashboard(request):
    if request.method == 'POST':
        # Login button has been pushed
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successfull login
            login(request, user)
            if Doctor.objects.filter(user_id=request.user.id).exists():
                # the user is authenticated and is a doctor
                messages.success(request, "You Have Been Logged In as a Doctor!")
                return redirect('doctor-dashboard')
            else:
                logout(request)
                messages.success(request, "You Are Not a Doctor, You Have Been Logged Out...")
                return redirect('home')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('doctor-dashboard')
    else:
        # request.method = GET form
        return render(request, 'doctor-dashboard.html', {})

def patient_dashboard(request):
    if request.method == 'POST':
        # Login button has been pushed
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successfull login
            login(request, user)
            if Patient.objects.filter(user_id=request.user.id).exists():
                # the user is authenticated and is a patient
                messages.success(request, "You Have Been Logged In as a Patient!")
                return redirect('patient-dashboard')
            else:
                logout(request)
                messages.success(request, "You Are Not a Patient, You Have Been Logged Out...")
                return redirect('home')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('patient-dashboard')
    else:
        # request.method = GET form
        return render(request, 'patient-dashboard.html', {})
    
def pharmacist_dashboard(request):
    if request.method == 'POST':
        # Login button has been pushed
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successfull login
            login(request, user)
            if Pharmacist.objects.filter(user_id=request.user.id).exists():
                # the user is authenticated and is a pharmacist
                messages.success(request, "You Have Been Logged In as a Pharmacist!")
                return redirect('pharmacist-dashboard')
            else:
                logout(request)
                messages.success(request, "You Are Not a Pharmacist, You Have Been Logged Out...")
                return redirect('home')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('pharmacist-dashboard')
    else:
        # request.method = GET form
        return render(request, 'pharmacist-dashboard.html', {})
    
def labtechnician_dashboard(request):
    if request.method == 'POST':
        # Login button has been pushed
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Successfull login
            login(request, user)
            if LabTechnician.objects.filter(user_id=request.user.id).exists():
                # the user is authenticated and is a pharmacist
                messages.success(request, "You Have Been Logged In as a Lab Technician!")
                return redirect('labtechnician-dashboard')
            else:
                logout(request)
                messages.success(request, "You Are Not a Lab Technician, You Have Been Logged Out...")
                return redirect('home')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('labtechnician-dashboard')
    else:
        # request.method = GET form
        return render(request, 'labtechnician-dashboard.html', {})

def patient_list(request):
    # request.method = GET form
    patients = Patient.objects.all()
    return render(request, 'patient-list.html', {'patients':patients})

def appointment_list(request):
    # request.method = GET form
    appointments = Appointment.objects.all()
    return render(request, 'appointment-list.html', {'appointments':appointments})

class AddPatientView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'add_patient.html'

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')