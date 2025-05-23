from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Patient, Appointment, Doctor, Pharmacist, LabTechnician, Sample, Prescription, Diagnose
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import PatientForm, EditPatientForm, DoctorAddAppointmentForm, DoctorUpdateAppointmentForm, SampleForm, PrescriptionForm, DiagnoseForm
from .forms import PatientAddAppointmentForm, PatientUpdateAppointmentForm
from django.urls import reverse_lazy
from django.urls import reverse

userParams = ["doctor", "patient", "lab-technician", "pharmacist"]
userTypes = [Doctor, Patient, LabTechnician, Pharmacist]

def getUserType(request):
    if request.user.is_authenticated:
        for i in range(4):
            if userTypes[i].objects.filter(user=request.user) :
                return userParams[i]
    return "all"

userParams = ["doctor", "patient", "lab-technician", "pharmacist"]
userTypes = [Doctor, Patient, LabTechnician, Pharmacist]

def getUserType(request):
    if request.user.is_authenticated:
        for i in range(4):
            if userTypes[i].objects.filter(user=request.user) :
                return userParams[i]
    return "all"

def home(request):
    return render(request, 'home.html', {'userType': getUserType(request)})

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

def patient_appointment_list(request):
    # request.method = GET form
    # Get the doctor object for the current user
    patient = Patient.objects.get(user_id=request.user.id)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patient-appointment-list.html', {'appointments':appointments})

class PatientAddAppointmentView(CreateView):
    model = Appointment
    form_class = PatientAddAppointmentForm
    template_name = 'patient-add-appointment.html'

    def get_success_url(self):
        return reverse('patient-appointment-list')
    # success_url = '/appointment-list/'

    def form_valid(self, form):
         # Set the patient to the current logged-in patient
         patient = Patient.objects.get(user_id=self.request.user.id)
         form.instance.patient = patient
         return super().form_valid(form)
    
class PatientUpdateAppointmentView(UpdateView):
    model = Appointment
    form_class = PatientUpdateAppointmentForm
    template_name = 'patient-edit-appointment.html'

    def get_success_url(self):
        return reverse('patient-appointment-list')
    
    def form_valid(self, form):
         # Set the patient to the current logged-in patient
         patient = Patient.objects.get(user_id=self.request.user.id)
         form.instance.patient = patient
         return super().form_valid(form)

class PatientDeleteAppointmentView(DeleteView):
    model = Appointment
    template_name = 'patient-delete-appointment.html'
    success_url = reverse_lazy('patient-appointment-list')
    
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

def appointment_list(request):
    # request.method = GET form
    # Get the doctor object for the current user
    doctor = Doctor.objects.get(user_id=request.user.id)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'appointment-list.html', {'appointments':appointments})

class DoctorAddAppointmentView(CreateView):
    model = Appointment
    form_class = DoctorAddAppointmentForm
    template_name = 'doctor-add-appointment.html'
    #success_url = '/appointment-list/'

    def form_valid(self, form):
        # Set the doctor to the current logged-in doctor
        doctor = Doctor.objects.get(user_id=self.request.user.id)
        form.instance.doctor = doctor
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('appointment-list')

class DoctorUpdateAppointmentView(UpdateView):
    model = Appointment
    form_class = DoctorUpdateAppointmentForm
    template_name = 'doctor-edit-appointment.html'

    def get_success_url(self):
        return reverse('appointment-list')
    

class DoctorDeleteAppointmentView(DeleteView):
     model = Appointment
     template_name = 'doctor-delete-appointment.html'
     success_url = reverse_lazy('appointment-list')

def patient_list(request):
    # request.method = GET form
    patients = Patient.objects.all()
    return render(request, 'patient-list.html', {'patients':patients})

class AddPatientView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'add_patient.html'

class UpdatePatientView(UpdateView):
    model = Patient
    form_class = EditPatientForm
    template_name = 'update-patient.html'

def sample_list(request):
    samples = Sample.objects.all()
    return render(request, 'sample-list.html', {'samples':samples})

class AddSampleView(CreateView):
    model = Sample
    form_class = SampleForm
    template_name = 'add-sample.html'

class UpdateSampleView(UpdateView):
    model = Sample
    form_class = SampleForm
    template_name = 'update-sample.html'

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescription-list.html', {'prescriptions':prescriptions, 'userType':getUserType(request)})

def prescription_list_doctor(request):
    prescriptions = Prescription.objects.filter(appointment__in=Appointment.objects.filter(doctor__in=Doctor.objects.filter(user=request.user)))
    return render(request, 'prescription-list.html', {'prescriptions':prescriptions, 'userType':getUserType(request)})

def prescription_list_patient(request):
    prescriptions = Prescription.objects.filter(appointment__in=Appointment.objects.filter(patient__in=Patient.objects.filter(user=request.user)))
    return render(request, 'prescription-list-patient.html', {'prescriptions':prescriptions})

class AddPrescriptionView(CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'add-prescription.html'

class UpdatePrescriptionView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'update-prescription.html'

def diagnose_list(request):
    diagnoses = Diagnose.objects.filter(appointment__in=Appointment.objects.filter(doctor__in=Doctor.objects.filter(user=request.user)))
    return render(request, 'diagnose-list.html', {'diagnoses':diagnoses})

def diagnose_list_patient(request):
    diagnoses = Diagnose.objects.filter(appointment__in=Appointment.objects.filter(patient__in=Patient.objects.filter(user=request.user)))
    return render(request, 'diagnose-list-patient.html', {'diagnoses':diagnoses})

class AddDiagnoseView(CreateView):
    model = Diagnose
    form_class = DiagnoseForm
    template_name = 'add-diagnose.html'

class UpdateDiagnoseView(UpdateView):
    model = Diagnose
    form_class = DiagnoseForm
    template_name = 'update-diagnose.html'

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')