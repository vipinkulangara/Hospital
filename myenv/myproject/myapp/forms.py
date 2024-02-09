from django import forms
from . models import Patient,Doctor,Login,Masteraccount,AdminMaster,PatientAppointment,DiseaseList,DepartmentSection

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {

        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        widgets = {

         }
class DoctorForm(forms.ModelForm):

    class Meta:

        model = Doctor
        fields = "__all__"
        widgets = {

                }
class AccountForm(forms.ModelForm):
    class Meta:
        model = Masteraccount
        fields = "__all__"
        widgets = {


                }

class MasterForm(forms.ModelForm):
    class Meta:
        model = AdminMaster
        fields = "__all__"
        widgets = {

         }
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = PatientAppointment
        fields = "__all__"
        widgets = {

        }
class DiseaseForm(forms.ModelForm):
    class Meta:
        model = DiseaseList
        fields = "__all__"
        widgets = {

                }
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentSection
        fields = "__all__"
        widgets = {

        }
        