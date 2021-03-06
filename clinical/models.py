from patient.models import Patient
from django.db import models
from physicing.models import physician

CLINICAL_RECORD_CHOISE = [
    (1, 'telorder'),
    (2, 'visit'),
    (3, 'tele-medecine'),
]

class Clinical_record(models.Model):
    patient_id      = models.ForeignKey(Patient,related_name="clinical_record", null=True ,on_delete =True)
    physician_id    = models.ForeignKey(physician,related_name="clinical_record", null=True ,on_delete =True)
    category        = models.IntegerField(choices = CLINICAL_RECORD_CHOISE)
    description     = models.TextField(verbose_name = None )
    data            = models.DateTimeField(auto_now =True)

    # class Meta:
    #     ordering = ('data')

    def __str__(self):
        return self.category

class medecine_order(models.Model):
    Clinical_record_id  = models.ForeignKey(Clinical_record,related_name="medecine_order", null=True ,on_delete =True)
    # medecine_id       = models.ForeignKey(Pedecine, null=True ,on_delete =True)
    patient_id          = models.ForeignKey(Patient,related_name="medecine_order", null=True ,on_delete =True)
    dose                = models.CharField(max_length = 150  )
    qty                 = models.IntegerField(verbose_name = None )
    description         = models.TextField(verbose_name = None )

    # class Meta:
    #     ordering = ('Clinical_record_id')

    # def __str__(self):
    #     return (ops_id)



class treatment_order(models.Model):
    Clinical_record_id  = models.ForeignKey(Clinical_record,related_name="treatment_order", null=True ,on_delete =True)
    patient_id          = models.ForeignKey(Patient,related_name="treatment_order", null=True ,on_delete =True)
    key                 = models.CharField(max_length=200)
    value               = models.TextField(verbose_name = None )
    description         = models.TextField(verbose_name = None )
    
    # class Meta:
    #     ordering = ('key')

    def __str__(self):
        return self.key