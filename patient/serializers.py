from rest_framework import serializers
from patient.models import Patient , Contact , Record ,Refrence


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'name',
            'family', 
            'national_code', 
            'birthday',
            'gender',
            'id'
            ]

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    class Meta:
        model = Contact
        fields = [
            'patient_id',
            'kay',
            'value',
            'id'
            ]

class RefrenceSerializer(serializers.HyperlinkedModelSerializer):
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
    
class RecordSerializer(serializers.HyperlinkedModelSerializer):
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


