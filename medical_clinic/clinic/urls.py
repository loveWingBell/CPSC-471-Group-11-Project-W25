from django.urls import path
from . import views
from .views import AddPatientView, UpdatePatientView

urlpatterns = [
    path("", views.home, name='home'),
    path("doctor-dashboard/", views.doctor_dashboard, name='doctor-dashboard'),
    path("patient-dashboard/", views.patient_dashboard, name='patient-dashboard'),
    path("pharmacist-dashboard/", views.pharmacist_dashboard, name='pharmacist-dashboard'),
    path("labtechnician-dashboard/", views.labtechnician_dashboard, name='labtechnician-dashboard'),
    path('add_patient/', AddPatientView.as_view(), name="add_patient"),
    path('patient/edit/<int:pk>', UpdatePatientView.as_view(), name='update-patient'),
    path("patient-list/", views.patient_list, name='patient-list'),
    path("appointment-list/", views.appointment_list, name='appointment-list'),
    path("logout/", views.logout_user, name='logout'),
]