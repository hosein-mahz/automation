from rest_framework import serializers
from .models import Invoice
from ParaClininical.models import Operation_record

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    Operation_record_id  = serializers.RelatedField(source='Operation_record', read_only=True)
    # physician_id = serializers.RelatedField(source='physician', read_only=True)
    
    class Meta:
        model = Invoice
        fields = [
            # 'physician_id',
            # 'patient_id', 
            'Operation_record_id'
            ]