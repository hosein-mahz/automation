from rest_framework import serializers
from physicing.models import physician

class physicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = physician
        fields = [
            'name',
            'degree', 
            'expert',
            'id' 
            ]