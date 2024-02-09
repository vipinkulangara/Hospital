from django.contrib import admin
from.models import Patient,Doctor,Login,PatientAppointment,AdminMaster,DiseaseList,DepartmentSection
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Login)
admin.site.register(PatientAppointment)
admin.site.register(AdminMaster)

admin.site.register(DepartmentSection)
admin.site.register(DiseaseList)