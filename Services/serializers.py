from rest_framework import serializers
from .models import Services
from physicing.models import physician
from patient.models import Patient

class ServicesSerializer(serializers.ModelSerializer):
    Service_list   = serializers.StringRelatedField(many=True)

    class Meta:
        model = Services
        fields = [   
            'category',
            'id',
            'Service_list'
            ]
