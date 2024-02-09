"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('patientRegistration',views.patientRegistration,name='patientRegistration'),
    path('LoginFrm',views.LoginFrm,name='login'),
    #path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('Signup',views.Signup,name='Signup'),
    path('appointment', views.appointment, name='appointment'),
    path('viewdisease', views.viewdisease, name='viewdisease'),
    path('Approveappointment', views.Approveappointment, name='Approveappointment'),

    path('UserModule', views.UserModule, name='UserModule'),
    path('DoctorModule', views.DoctorModule, name='DoctorModule'),

    path('DoctorRegistration',views.DoctorRegistration,name='DoctorRegistration'),
    path('viewdoctor',views.viewdoctor,name='viewdoctor'),
    path('viewappointment',views.viewappointment,name='viewappointment'),
    path('AdminModule',views.AdminModule,name='AdminModule'),
    path('viewpatient',views.viewpatient,name='viewpatient'),
    path('viewdepartment', views.viewdepartment, name='viewdepartment'),
    path('Department', views.Department, name='Department'),
    path('findDoctor',views.findDoctor,name='findDoctor'),
    path('AproveADMIN',views.AproveADMIN,name='AproveADMIN'),
    path('viewappointment', views.viewappointment, name='viewappointment'),
    path('editappointment/<int:id>', views.editappointment, name='editappointment'),
    path('updateappointment/<int:id>', views.updateappointment, name='updateappointment'),
    path('deleteappointment/<int:id>', views.deleteappointment, name='deleteappointment'),
]
