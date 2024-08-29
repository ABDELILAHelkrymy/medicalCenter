from django.contrib import admin
from django.urls import path
from .views import doctorGetById, doctorGetAll, doctorAdd, doctorDelete, appoitementAdd, appoitementGetAll

urlpatterns = [
    path('doctorById/<str:pk>/', doctorGetById, name='doctorById'),
    path('doctorGetAll/', doctorGetAll, name='doctorGetAll'),
    path('doctorAdd/', doctorAdd, name='doctorAdd'),
    path('doctorDelete/<str:pk>/', doctorDelete, name='doctorDelete'),
    path('patientGetAll/', appoitementAdd, name='patientGetAll'),
    path('appoitementAdd/', appoitementAdd, name='appoitementAdd'),
    path('appoitementGetAll/', appoitementGetAll, name='appoitementGetAll'),
]
