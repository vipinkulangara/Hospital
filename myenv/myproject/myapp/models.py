from django.db import models

# Create your models here.
class Patient(models.Model):
    patientname=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    contactnum=models.CharField(max_length=100)
    disease=models.CharField(max_length=150,null=True,blank=True)
    doctorname=models.CharField(max_length=150,null=True,blank=True)
    username=models.CharField(max_length=150,null=True,blank=True)
    password=models.CharField(max_length=150,null=True,blank=True)
    status=models.CharField(max_length=150,null=True,blank=True)
    def __str__(self):
        return self.patientname

class Login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return self.username
    
class Doctor(models.Model):
    specilization = models.CharField(max_length=150)
    doctorname = models.CharField(max_length=150)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    maritalstatus = models.CharField(max_length=150)
    visittime = models.CharField(max_length=150)
    days = models.CharField(max_length=150)
    username = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return self.doctorname


    
class AdminMaster(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return self.username

class Masteraccount(models.Model):
    name=models.CharField(max_length=150)
    contactnum=models.CharField(max_length=150)
    mail=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    confirmpassword=models.CharField(max_length=150)
    def __str__(self):
        return self.name
class PatientAppointment(models.Model):
    patientname=models.CharField(max_length=100)
    contactnum = models.CharField(max_length=100)
    age=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    doctorname = models.CharField(max_length=100,null=True,blank=True)
    date = models.CharField(max_length=100,null=True,blank=True)
    symptoms=models.CharField(max_length=150,null=True,blank=True)
    def __str__(self):
        return self.patientname
class DiseaseList(models.Model):
    diseasename=models.CharField(max_length=150)
    symptoms=models.CharField(max_length=150)
    doctorname=models.CharField(max_length=150)
    def __str__(self):
        return self.diseasename
class DepartmentSection(models.Model):
    departmentnumber=models.CharField(max_length=150)
    departmentname=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    def __str__(self):
        return self.departmentname
    