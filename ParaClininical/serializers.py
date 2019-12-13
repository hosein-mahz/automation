from rest_framework import serializers
from ParaClininical.models import Classtreatment_order, Consumable_order,device_order,Hoteling,Medecine_order,Operation_record,Service_list
from physicing.models import physician
from patient.models import Patient
from Services.models import Services


class Operation_recordSerializer(serializers.HyperlinkedModelSerializer):
    patient_id = serializers.RelatedField(source='Patient', read_only=True)
    physician_id = serializers.RelatedField(source='physician', read_only=True)
    
    class Meta:
        model = Operation_record
        fields = [
            'physician_id',
            'patient_id', 
            'title',
            'data'
            ]

class Service_listSerializer(serializers.HyperlinkedModelSerializer):
    service_id = serializers.RelatedField(source='service', read_only=True)
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = Service_list
        fields = [
            'Operation_record_id',
            'service_id', 
            'qty',
            'description '
            ]

class Medecine_orderSerializer(serializers.HyperlinkedModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    # service_id = serializers.RelatedField(source='service', read_only=True)
    
    class Meta:
        model = Medecine_order
        fields = [
            'Operation_record_id',
            # ' medecine_id', 
            'dose',
            'qty',
            'description '
            ]
            
class Classtreatment_orderSerializer(serializers.HyperlinkedModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    # service_id = serializers.RelatedField(source='service', read_only=True)
    
    class Meta:
        model = Medecine_order
        fields = [
            'Operation_record_id',
            # 'medecine_id', 
            'dose',
            'value',
            'description '
            ]

class Consumable_orderSerializer(serializers.HyperlinkedModelSerializer):
    # consumable_id = serializers.RelatedField(source='service', read_only=True)
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = Service_list
        fields = [
            'Operation_record_id',
            # 'consumable_id', 
            'qty',
            'description '
            ]
            
class device_orderSerializer(serializers.HyperlinkedModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = device_order
        fields = [
            'Operation_record_id',
            'title', 
            'qty',
            'description '
            ]

class HotelingSerializer(serializers.HyperlinkedModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = Hoteling
        fields = [
            'Operation_record_id',
            'title', 
            'qty',
            'description '
            ]