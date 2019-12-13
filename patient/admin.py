from django.contrib import admin
from .models import Patient, Refrence, Contact, Record

admin.site.register([Patient, Refrence, Contact, Record])
