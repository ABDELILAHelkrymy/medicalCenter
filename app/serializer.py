from rest_framework import serializers
from .models import Doctor, Patient, Appoitement

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','name', 'email', 'speciality']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','name', 'email']


class AppoitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoitement
        fields = ['id','doctorId', 'patientId', 'dateAppoitement']
