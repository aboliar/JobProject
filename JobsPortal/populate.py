import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JobsPortal.settings')
import django
django.setup()

from demoapp.models import *
from random import *
from faker import Faker
fobj = Faker()

def mobnogen():
    x = randint(7,9)
    num = str(x)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fobj.date()
        fcompany = fobj.company()
        ftitle = fobj.random_element(elements=('DBA','Team Lead','Software Engineer',
        'Fullstack Developer'))
        feligibility = fobj.random_element(elements=('B.Tech','M.Tech','MCA'))
        faddress = fobj.address()
        femail = fobj.email()
        fmobno = mobnogen()
        #punejob_records = PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,mobno=fmobno)
        mumbaijob_records = MumbaiJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,mobno=fmobno)
populate(50)
