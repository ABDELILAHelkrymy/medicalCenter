from django.shortcuts import render, HttpResponse
from .models import Doctor, Patient, Appoitement
from .serializer import DoctorSerializer, PatientSerializer, AppoitementSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# get doctor list
@api_view(['GET'])
def doctorGetAll(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

# get doctor by id
@api_view(['GET'])
def doctorGetById(request, pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)

# add doctor
@api_view(['POST'])
def doctorAdd(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete doctor
@api_view(['DELETE'])
def doctorDelete(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return Response('Doctor deleted')

# get patient list
@api_view(['GET'])
def patientGetAll(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


# make appoitement
@api_view(['POST'])
def appoitementAdd(request):
    serializer = AppoitementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# get appoitement list 
@api_view(['GET'])
def appoitementGetAll(request):
    appoitements = Appoitement.objects.all()
    serializer = AppoitementSerializer(appoitements, many=True)
    return Response(serializer.data)
