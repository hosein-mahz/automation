from django.http import HttpResponse, JsonResponse
from django.core import serializers
from patient.models import Record
from patient.models import Patient
from json import loads
from patient.models import Refrence
from rest_framework import viewsets
from patient.serializers import RecordSerializer



def convertToJson(_QuerySet):
    g = serializers.serialize("json", _QuerySet)
    _data = loads(g) 
    return _data


def dev(request):
    data = convertToJson(Patient.objects.all())
    return JsonResponse(data, safe=False)


def helperId(_object):
    _object['fields']['id']=_object['pk']
    return _object
  
def helperId(_object):
    _object['fields']['id']=_object['pk']
    return _object

# /////////////////////////////////////////////////////

def getAll(request):
    data = convertToJson(Record.objects.all())
    for x in data:
        l = convertToJson(Record.objects.get(pk=x['pk']).Patient_set.all() )
        l = helperId(l)
        x['fields']['Patient'] = []
        for y in l:
            x['fields']['Patient'].append(y['fields'])
        
    return JsonResponse(data, safe=False)


def getSingle(request, _id):
    data = convertToJson( Record.objects.get(id=_id) )
    data[0] = helperId(data[0])
    return JsonResponse(data[0]['fields'], safe=False)

def create(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            if data['name'] == '' or hasattr(data, 'name') :
                return JsonResponse({'message':'unsuccessful createing'}, safe=False)
                _Record = Record(
                patient_id  = data['patient_id'],
                kay         = data['kay'],
                value       = data['value'],
                time        = data['time'],
                start_date  = data['end_date'],
                end_date    = data['end_date'],
                )
            _Contact.save()
            return JsonResponse({'message':'successful create new Record'}, safe=False)
        except:
            return JsonResponse({'message':'unsuccessful createing'}, safe=False)
    return JsonResponse({'message': 'most use POST method'}, safe=False)

def delete(request, _id): 
    if request.method == 'DELETE':
        try:
            Record.objects.filter(pk=_id).delete()
            return JsonResponse({'message': 'successfull deleting'}, safe=False)
        except:
            return JsonResponse({'message': 'unsuccessfull deleting'}, safe=False)
    return JsonResponse({'message': 'most use DELETE method'}, safe=False)

def update(request, _id):
    if request.method == 'PUT':
        try:
            data = loads(request.body)
            Record.objects.filter(id=_id).update(
                patient_id  = data['patient_id'],
                kay         = data['kay'],
                value       = data['value'],
                time        = data['time'],
                start_date  = data['end_date'],
                end_date    = data['end_date'],
            )
            return JsonResponse({'message': 'successfull updating'}, safe=False)
        except : 
            return JsonResponse({'message': 'unsuccessfull updating'}, safe=False)

# /////////////////////////////////////////////////////
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-time')
    serializer_class = RecordSerializer