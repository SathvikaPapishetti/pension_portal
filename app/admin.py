from django.contrib import admin
from sih_app.models import emp, otherdata,nsapdata, nopension
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display=['emp_fname','emp_lname','emp_email']
admin.site.register(emp,employeeAdmin)
admin.site.register(otherdata)
admin.site.register(nsapdata)
admin.site.register(nopension)
