from django.db import models

class Patient (models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    national_code = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name 

class Refrence (models.Model):
    patient_id = models.OneToManyField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    # dare = models.CharField(max_length=30)

    class meta:
        ordering = ('patient_id')

    def __str__(self):
        return self.name

RECORD_CHOISE = [
    (1, 'Freshman'),
    (2, 'Sophomore'),
    (3, 'Junior'),
    (4, 'Senior'),
]

class Record (models.Model):
    patient_id = models.OneToOneField(Patient)
    time = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=160, choices=RECORD_CHOISE)
    value = models.CharField(max_length=30)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.CharField(max_length=30)

    class meta:
        ordering = ('start_data')

    def __str__(self):
        return self.start_date
    