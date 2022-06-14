from django.db import models

class DataPatient(models.Model):
    patient = models.CharField(max_length=200)
    age = models.IntegerField()
    neurological = models.IntegerField()
    cardiovascular = models.IntegerField()
    respiratory = models.IntegerField()
    coagulation = models.IntegerField()
    hepatic = models.IntegerField()
    renal = models.IntegerField()
    icc = models.IntegerField()
    ecog = models.IntegerField()
    classification = models.IntegerField()
