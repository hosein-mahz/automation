from rest_framework import serializers
from .models import Services
from physicing.models import physician
from patient.models import Patient

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    # patient_id = serializers.RelatedField(source='Patient', read_only=True)
    # physician_id = serializers.RelatedField(source='physician', read_only=True)
    
    class Meta:
        model = Services
        fields = [
            # 'physician_id',
            # 'patient_id', 
            'category'
            ]
