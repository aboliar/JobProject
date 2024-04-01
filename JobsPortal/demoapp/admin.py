from django.contrib import admin
from demoapp.models import *

# Register your models here.
class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','eligibility','address','email','mobno']

class MumbaiJobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','eligibility','address','email','mobno']


admin.site.register(PuneJobs,PuneJobsAdmin)
admin.site.register(MumbaiJobs,MumbaiJobsAdmin)
