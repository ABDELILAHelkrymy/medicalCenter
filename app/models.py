from django.db import models
import uuid
import datetime
from django.db import models
import uuid


class Doctor(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    speciality = models.CharField(max_length=100, blank=False, null=False)

class Patient(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)

class Appoitement(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dateAppoitement = models.DateField(default=datetime.datetime.now, blank=False, null=False)

