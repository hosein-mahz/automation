from django.db import models
from patient.models import Patient
from physicing.models import physician
from Services.models import Services


class Operation_record(models.Model):
    patient_id      = models.ForeignKey(Patient, null=True ,on_delete =True)
    physician_id    = models.ForeignKey(Physician, null=True ,on_delete =True)
    data            = models.DateTimeField(auto_now =True)
    title           = models.CharField(max_length=280)

    class Meta:
        ordering = ('data')

    def __str__(self):
        return self.title 

class Service_list(models.Model):
    Operation_record_id  = models.ForeignKey(Operation_record, null =True ,on_delete  =True)
    service_id         = models.ForeignKey(Service, null=True ,on_delete  =True)
    qty                  = models.IntegerField(verbose_name= None )
    description          = models.TextField(verbose_name= None )
    
    class Meta:
        ordering = ('service_id')

    def __str__(self):
        return self.title 

    class Medecine_order(models.Model):
        Operation_record_id                 = models.ForeignKey(Operation_record, null =True ,on_delete  =True)
        # medecine_id                       = models.ForeignKey(Medecine, null=True ,on_delete  =True)
        dose                                = models.CharField(max_length= 150 )
        qty                                 = models.IntegerField(verbose_name= None )
        description                         = models.TextField(verbose_name= None )
    
    class Meta:
        ordering = ('dose')

    # def __str__(self):
    #     return self.title

class Classtreatment_order(models.Model):
    Operation_record_id = models.ForeignKey(Operation_record, null=True ,on_delete =True)
    key                 = models.CharField(max_length=200)
    value               = models.TextField(verbose_name = None )
    description         = models.TextField(verbose_name = None )

    
    class Meta:
        ordering = ('key')

    # def __str__(self):
    #     return self.title

class Consumable_order(models.Model):
    Operation_record_id  = models.ForeignKey(Operation_record, null =True ,on_delete=True)
    # consumable_id      = models.ForeignKey(Consumable, null=True ,on_delete  =True)
    qty                  = models.IntegerField(verbose_name= None )
    description          = models.TextField(verbose_name= None )

class device_order(models.Model):
    Operation_record_id  = models.ForeignKey(Operation_record, null =True ,on_delete  =True)
    title                = models.CharField(max_length=280)
    qty                  = models.IntegerField(verbose_name= None )
    description          = models.TextField(verbose_name= None )

    class Meta:
        ordering = ('qty')

    def __str__(self):
        return self.title


TITLE_CHOISE = [
    (1, '1-2'),
    (2, '2-4'),
]

class Hoteling (models.Model):
    Operation_record_id  = models.ForeignKey(Operation_record, null =True ,on_delete =True)
    title                = models.IntegerField(max_length=160, choices=TITLE_CHOISE)
    description          = models.TextField(verbose_name = None )
    qty                  = models.IntegerField(verbose_name = None )

    
    class Meta:
        ordering = ('qty')

    def __str__(self):
        return self.title

