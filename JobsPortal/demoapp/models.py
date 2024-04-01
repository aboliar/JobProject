from django.db import models

# Create your models here.
class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    eligibility = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobno = models.IntegerField()

class MumbaiJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    eligibility = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    mobno = models.IntegerField()
