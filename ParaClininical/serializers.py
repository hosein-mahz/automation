from rest_framework import serializers
from ParaClininical.models import Classtreatment_order, Consumable_order,device_order,Hoteling,Medecine_order,Operation_record,Service_list
from physicing.models import physician
from patient.models import Patient
from Services.models import Services


class Operation_recordSerializer(serializers.ModelSerializer):
    hoteling               = serializers.StringRelatedField(many=True)
    device_order           = serializers.StringRelatedField(many=True)
    consumable_order       = serializers.StringRelatedField(many=True)
    classtreatment_order   = serializers.StringRelatedField(many=True)
    medecine_order         = serializers.StringRelatedField(many=True)
    Service_list           = serializers.StringRelatedField(many=True)
    invoice           = serializers.StringRelatedField(many=True)

    class Meta:
        model = Operation_record
        fields = [
            'physician_id',
            'patient_id', 
            'title',
            'data',
            'id',
            'Service_list',
            'medecine_order',
            'classtreatment_order',
            'consumable_order',
            'device_order',
            'Hoteling',
            'invoice'
            ]

class Service_listSerializer(serializers.ModelSerializer):
    service_id = serializers.RelatedField(source='service', read_only=True)
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = Service_list
        fields = [
            'Operation_record_id',
            'service_id', 
            'qty',
            'description',
            'id'
            ]

class Medecine_orderSerializer(serializers.ModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    # service_id = serializers.RelatedField(source='service', read_only=True)
    
    class Meta:
        model = Medecine_order
        fields = [
            'Operation_record_id',
            # ' medecine_id', 
            'dose',
            'qty',
            'description',
            'id'
            ]
            
class Classtreatment_orderSerializer(serializers.ModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    # service_id = serializers.RelatedField(source='service', read_only=True)
    
    class Meta:
        model = Classtreatment_order
        fields = [
            'Operation_record_id',
            # 'medecine_id', 
            'key',
            'value',
            'description',
            'id'
            ]

class Consumable_orderSerializer(serializers.ModelSerializer):
    # consumable_id = serializers.RelatedField(source='service', read_only=True)
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = Service_list
        fields = [
            'Operation_record_id',
            # 'consumable_id', 
            'qty',
            'description',
            'id'
            ]
            
class device_orderSerializer(serializers.ModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = device_order
        fields = [
            'Operation_record_id',
            'title', 
            'qty',
            'description',
            'id'
            ]

class HotelingSerializer(serializers.ModelSerializer):
    Operation_record_id = serializers.RelatedField(source='Operation_record', read_only=True)
    
    class Meta:
        model = Hoteling
        fields = [
            'Operation_record_id',
            'title', 
            'qty',
            'description',
            'id'
            ]