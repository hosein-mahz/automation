from rest_framework import serializers
from clinical.models import Clinical_record , medecine_order , treatment_order
from physicing.models import physician
from patient.models import Patient

class Clinical_recordSerializer(serializers.ModelSerializer):
    medecine_order   = serializers.StringRelatedField(many=True) 
    treatment_order   = serializers.StringRelatedField(many=True)

    class Meta:
        model = Clinical_record
        fields = [
            'patient_id',
            'physician_id', 
            'category', 
            'description',
            'data',
            'id',
            'treatment_order',
            'medecine_order'
            ]


class medecine_orderSerializer(serializers.ModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    physician_id = serializers.RelatedField(source='physician', read_only=True)
    class Meta:
        model = medecine_order
        fields = [
            'Clinical_record_id',
            # 'medecine_id', 
            'patient_id', 
            'dose',
            'qty',
            'description',
            'id'
            ]

class treatment_orderSerializer(serializers.ModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    Clinical_record_id = serializers.RelatedField(source='Clinical_record', read_only=True)
    
    class Meta:
        model = treatment_order
        fields = [
            'Clinical_record_id', 
            'patient_id', 
            'key',
            'value',
            'description',
            'id'
            ]
