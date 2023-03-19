from django.db import models

class BankClient(models.Model):
    age = models.IntegerField()
    job = models.CharField(max_length=100)
    marital = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    housing = models.CharField(max_length=100)
    loan = models.CharField(max_length=100)
    campaign = models.IntegerField()
    previous = models.IntegerField()
    poutcome = models.CharField(max_length=100)
    empvarrate = models.FloatField()
    conspriceidx = models.FloatField()
    consconfidx = models.FloatField()
    euribor3m = models.FloatField() 
    nremployed = models.FloatField()

class Label(models.Model):
    label = models.IntegerField()




# Create your models here.
