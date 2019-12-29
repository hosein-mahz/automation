from django.db import models
from ParaClininical.models import Operation_record

class Invoice(models.Model):
    Operation_record_id  = models.ForeignKey(Operation_record,related_name="invoice", null =True ,on_delete  =True)
