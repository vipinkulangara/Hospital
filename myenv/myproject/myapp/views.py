from django.shortcuts import render,redirect
#from django.http import HttpResponse
from.forms import PatientForm,LoginForm,DoctorForm,AccountForm,AppointmentForm,DiseaseForm
from .models import Patient,Doctor,Login,AdminMaster,PatientAppointment,DiseaseList
# Create your views here.

#def home(request):
   # return HttpResponse('hello world','home.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return  render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')



def patientRegistration(request):
    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=PatientForm()
    return render(request,'patientRegistration.html')


def DoctorRegistration(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/viewdoctor")
    else:
        form = DoctorForm()
    return render(request, 'DoctorRegistration.html')

def viewdoctor(request):
    return render(request,'viewdoctor.html')

def LoginFrm(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form['username'].valid()
            password=form['password'].valid()
            try:
                user=Login.objects.get(username=username,password=password)
                if user is not None:
                    return render(request,'home.html')
            except:
               pass
    else:
        return render(request, 'LoginFrm.html')


'''def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'UserModule.html')
            return render(request, 'Signup.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'home.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'DoctorModule.html')
            return render(request,'Signup.html')
        except:
            pass
    else:
       return render(request,'Signup.html')'''

def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'UserModule.html')
            return render(request, 'Signup.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'home.html')
           #return render(request,'Adminmodule.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'DoctorModule.html')
            return render(request,'Signup.html')
        except:
             pass
    else:
        return render(request,'Signup.html')




def UserModule(request):
    return render(request,'UserModule.html')
def DoctorModule(request):
    return render(request,'DoctorModule.html')

def Newaccount(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = AccountForm()
    return render(request,'Newaccount.html')
def appointment(request):
    if request.method=="POST":
            form=AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'home.html')
    else:
        form=AppointmentForm()
    return render(request,'appointment.html')
def viewdisease(request):
    result = DiseaseList.objects.all()
    return render(request,'viewdisease.html',{'result':result})
def Approveappointment(request):
    return render(request,'Approveappointment.html')

def PatientEnquiry(request):
    if request.method=="POST":
        form=PatientAppointment(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=DiseaseForm()
        return render(request,'PatientEnquiry.html')

def viewappointment(request):
    result = PatientAppointment.objects.all()
    return render(request,'viewappointment.html', {'result': result})
def AdminModule(request):
    return render(request,'AdminModule.html')

def viewpatient(request):
    return render(request,'viewpatient.html')
def viewdepartment(request):
    return render(request,'viewdepartment.html')
#def login(request):
 #   return render(request,'login.html')

def Department(request):
    return render(request,'Department.html')

def findDoctor(request):
    return render(request,'findDoctor.html')
def AproveADMIN(request):
    return render(request,'AproveADMIN.html')
def viewpatient(request):
    result = Patient.objects.all()
    return render(request,'viewpatient.html', {'result': result})
def editpatient(request,id):
    result = Patient.objects.get(id=id)
    return render(request,'editpatient.html', {'result': result})

def deletepatient(request,id):
    result=Patient.objects.get(id=id)
    result.delete()
    return redirect('/viewpatient')


def updatepatient(request, id):
    result=Patient.objects.get(id=id)
    form=PatientForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/viewpatient')
    return render(request, 'editpatient.html', {'result': result})



def deleteappointment(request,id):
    result=PatientAppointment.objects.get(id=id)
    result.delete()
    return redirect('/viewappointment')
def editappointment(request,id):
    result = PatientAppointment.objects.get(id=id)
    return render(request,'editappointment.html', {'result': result})



def updateappointment(request,id):
    result=PatientAppointment.objects.get(id=id)
    form=AppointmentForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/viewappointment')
    return render(request, 'editappointment.html', {'result': result})
def viewappointment(request):
    result = PatientAppointment.objects.all()
    return render(request,'viewappointment.html', {'result': result})
