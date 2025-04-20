from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("doctor-dashboard/", views.doctor_dashboard, name='doctor-dashboard'),
    path("patient-dashboard/", views.patient_dashboard, name='patient-dashboard'),
    path("pharmacist-dashboard/", views.pharmacist_dashboard, name='pharmacist-dashboard'),
    path("labtechnician-dashboard/", views.labtechnician_dashboard, name='labtechnician-dashboard'),
    path("logout/", views.logout_user, name='logout'),

]