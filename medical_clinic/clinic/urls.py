from django.urls import path
from . import views
from .views import AddPatientView, UpdatePatientView, DoctorAddAppointmentView, DoctorUpdateAppointmentView, DoctorDeleteAppointmentView, AddSampleView, UpdateSampleView, AddPrescriptionView, UpdatePrescriptionView

urlpatterns = [
    path("", views.home, name='home'),
    path("doctor-dashboard/", views.doctor_dashboard, name='doctor-dashboard'),
    path("patient-dashboard/", views.patient_dashboard, name='patient-dashboard'),
    path("patient-appointment-list/", views.patient_appointment_list, name='patient-appointment-list'),
    path("pharmacist-dashboard/", views.pharmacist_dashboard, name='pharmacist-dashboard'),
    path("labtechnician-dashboard/", views.labtechnician_dashboard, name='labtechnician-dashboard'),

    path("patient-list/", views.patient_list, name='patient-list'),
    path('add_patient/', AddPatientView.as_view(), name="add_patient"),
    path('patient/edit/<int:pk>', UpdatePatientView.as_view(), name='update-patient'),

    path("appointment-list/", views.appointment_list, name='appointment-list'),
    path('doctor-add-appointment/', DoctorAddAppointmentView.as_view(), name="doctor-add-appointment"),
    path('doctor-appointment/edit/<int:pk>', DoctorUpdateAppointmentView.as_view(), name='doctor-edit-appointment'),
    path('doctor-appointment/<int:pk>/remove', DoctorDeleteAppointmentView.as_view(), name='doctor-delete-appointment'),
    path("logout/", views.logout_user, name='logout'),

    path('sample-list/', views.sample_list, name='sample-list'),
    path('add-sample/', AddSampleView.as_view(), name="add-sample"),
    path('sample/edit/<int:pk>', UpdateSampleView.as_view(), name='update-sample'),

    path('prescription-list/', views.prescription_list, name='prescription-list'),
    path('add-prescription/', AddPrescriptionView.as_view(), name="add-prescription"),
    path('prescription/edit/<int:pk>', UpdatePrescriptionView.as_view(), name='update-prescription')
]