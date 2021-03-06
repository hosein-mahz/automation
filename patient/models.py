from django.db import models

PATIENT_CHOISE = [
    (1, 'men'),
    (2, 'women'),
]
class Patient (models.Model):
    name           = models.CharField(max_length=100)
    family         = models.CharField(max_length=100)
    national_code  = models.CharField(max_length=15)
    birthday       = models.DateTimeField(auto_now=True)
    gender         = models.IntegerField(choices=PATIENT_CHOISE)
    # id             = models.
    # class Meta:
    #     ordering = ('name')

    def __str__(self):
        return self.name 

CONTACT_CHOISE = [
    (1, 'adress'),
    (2, 'email'),
    (3, 'phone'),
]

class Contact (models.Model):
    patient_id  = models.ForeignKey(Patient,related_name="contact", null=True ,on_delete=models.CASCADE)
    kay         = models.IntegerField(choices=CONTACT_CHOISE)
    value       = models.TextField(verbose_name= None )
    
class Refrence (models.Model):
    patient_id  = models.ForeignKey(Patient,related_name='refrence', null=True, on_delete=True )
    name        = models.CharField(max_length=150)
    phone       = models.CharField(max_length=30)
    # dare = models.CharField(max_length=30)

    def __str__(self):
        return self.name

RECORD_CHOISE = [
    (1, 'Freshman'),
    (2, 'Sophomore'),
    (3, 'Junior'),
    (4, 'Senior'),
]

class Record (models.Model):
    patient_id  = models.ForeignKey(Patient,related_name="record", null =True ,on_delete=True )
    key         = models.IntegerField(choices=RECORD_CHOISE)
    value       = models.TextField(verbose_name= None )
    time        = models.DateTimeField(auto_now=True)
    start_date  = models.DateTimeField(auto_now=True)
    end_date    = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ('start_data')

    def __str__(self):
        return self.start_date
     