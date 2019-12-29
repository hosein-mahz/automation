from rest_framework import serializers
from physicing.models import physician

class physicianSerializer(serializers.ModelSerializer):
    clinical_record   = serializers.StringRelatedField(many=True)
    Operation_record   = serializers.StringRelatedField(many=True) 
    class Meta:
        model = physician
        fields = [
            'id', 
            'name',
            'degree', 
            'expert',
            'clinical_record',
            'Operation_record'
            ]