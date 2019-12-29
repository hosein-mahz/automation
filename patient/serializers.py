from rest_framework import serializers
from patient.models import Patient , Contact , Record ,Refrence


class PatientSerializer(serializers.ModelSerializer):
    record   = serializers.StringRelatedField(many=True)
    refrence = serializers.StringRelatedField(many=True)
    contact  = serializers.StringRelatedField(many=True)
    clinical_record  = serializers.StringRelatedField(many=True)
    treatment_order  = serializers.StringRelatedField(many=True)
    medecine_order   = serializers.StringRelatedField(many=True)
    operation_record       = serializers.StringRelatedField(many=True)    

    class Meta:
        model = Patient
        fields = [
            'id',
            'name',
            'family', 
            'national_code', 
            'birthday',
            'gender',
            'record',
            'refrence',
            'contact',
            'clinical_record',
            'treatment_order',
            'medecine_order' ,
            'operation_record'
            ] 

class ContactSerializer(serializers.ModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    class Meta:
        model = Contact
        fields = [
            'patient_id',
            'kay',
            'value',
            'id'
            ]

class RefrenceSerializer(serializers.ModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    # patient_id = serializers.StringRelatedField(many=False)
    # patient_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Refrence
        fields = [
            'patient_id', 
            'name',
            'phone',
            'id'
            ]
    
class RecordSerializer(serializers.ModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    class Meta:
        model = Record
        fields = [
            'patient_id', 
            'key',
            'value',
            'time',
            'start_date',
            'end_date',
            'id'
            ]


