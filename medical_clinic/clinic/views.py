from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient
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
            messages.success(request, "You Have Been Logged In!")
            return redirect('doctor-dashboard')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('doctor-dashboard')
    else:
        # request.method = GET form
        patients = Patient.objects.all()
        return render(request, 'doctor-dashboard.html', {'patients':patients})

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
            messages.success(request, "You Have Been Logged In!")
            return redirect('patient-dashboard')
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
            messages.success(request, "You Have Been Logged In!")
            return redirect('pharmacist-dashboard')
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
            messages.success(request, "You Have Been Logged In!")
            return redirect('labtechnician-dashboard')
        else:
            # Failed login attempt
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('labtechnician-dashboard')
    else:
        # request.method = GET form
        return render(request, 'labtechnician-dashboard.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

class AddPatientView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'add_patient.html'
