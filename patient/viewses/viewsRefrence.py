from django.http import HttpResponse, JsonResponse
from django.core import serializers
from patient.models import Refrence
from patient.models import Patient
from json import loads
from patient.models import Refrence
from rest_framework import viewsets
from patient.serializers import RefrenceSerializer



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
    data = convertToJson(Refrence.objects.all())
    for x in data:
        l = convertToJson(Refrence.objects.get(pk=x['pk']).Patient_set.all() )
        l = helperId(l)
        x['fields']['Patient'] = []
        for y in l:
            x['fields']['Patient'].append(y['fields'])
        
    return JsonResponse(data, safe=False)


def getSingle(request, _id):
    data = convertToJson( Refrence.objects.get(id=_id) )
    data[0] = helperId(data[0])
    return JsonResponse(data[0]['fields'], safe=False)

def create(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            if data['name'] == '' or hasattr(data, 'name') :
                return JsonResponse({'message':'unsuccessful createing'}, safe=False)
            _Refrence = Refrence(
                patient_id = data['patient_id'],
                name       = data['name'],
                phone      = data['phone']
            )
            _Contact.save()
            return JsonResponse({'message':'successful create new Refrence'}, safe=False)
        except:
            return JsonResponse({'message':'unsuccessful createing'}, safe=False)
    return JsonResponse({'message': 'most use POST method'}, safe=False)

def delete(request, _id): 
    if request.method == 'DELETE':
        try:
            Refrence.objects.filter(pk=_id).delete()
            return JsonResponse({'message': 'successfull deleting'}, safe=False)
        except:
            return JsonResponse({'message': 'unsuccessfull deleting'}, safe=False)
    return JsonResponse({'message': 'most use DELETE method'}, safe=False)

def update(request, _id):
    if request.method == 'PUT':
        try:
            data = loads(request.body)
            Contact.objects.filter(id=_id).update(
                patient_id = data['patient_id'],
                name       = data['name'],
                phone      = data['phone'],
                )
            return JsonResponse({'message': 'successfull updating'}, safe=False)
        except : 
            return JsonResponse({'message': 'unsuccessfull updating'}, safe=False)

# /////////////////////////////////////////////////////

class RefrenceViewSet(viewsets.ModelViewSet):
    queryset = Refrence.objects.all().order_by('-name')
    serializer_class = RefrenceSerializer