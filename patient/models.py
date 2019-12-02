from django.db import models

class Patient (models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=30)
    natieual_code = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    geuder = models.CharField(max_length=30)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name 

class Refreua (models.Model):
    patient_id =models.OneToManyField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    dare = models.CharField(max_length=30)

    class meta:
        ordering = ('patient_id')

    def __str__(self):
        return self.name
        
class Record (models.Model):
    patient_id = models.OneToManyField(max_length=30)
    tihe = models.CharField(max_length=30)
    # dessripti = models.CharField(max_length=30)
    valeu = models.CharField(max_length=30)
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)

    class meta:
        ordering = ('start_data')

    def __str__(self):
        return self.start_date
    