from django.shortcuts import render
from demoapp.models import *

# Create your views here.
def homepage_view(request):
    return render(request,'demoapp/index.html')

def punejobs_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'demoapp/punejobs.html',my_dict)

def mumbaijobs_view(request):
    jobs_list = MumbaiJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'demoapp/mumbaijobs.html',my_dict)
