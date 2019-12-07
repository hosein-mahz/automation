from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Patient
from json import loads

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

# /////////////////////////////////////////////////////

def getAll(request):
    data = convertToJson(Patient.objects.all())   
    return JsonResponse(data, safe=False)


def getSingle(request, _id):
    data = convertToJson(Patient.objects.get(id=_id) )
    data[0] = helperId(data[0])
    return JsonResponse(data[0]['fields'], safe=False)


def create(request):
    if request.method == 'POST':
        try:
            data = loads(request.body)
            if data['name'] == '' or hasattr(data, 'name') :
                return JsonResponse({'message':'unsuccessful createing'}, safe=False)
            _Patient = Patient(
                name = data['name'],
                family = data['family'],
                national_code = data['national_code'],
                birthday = data['birthday'],
                gender = data['gender']
                )
            _Patient.save()
            return JsonResponse({'message':'successful create new Patient'}, safe=False)
        except:
            return JsonResponse({'message':'unsuccessful createing'}, safe=False)
    return JsonResponse({'message': 'most use POST method'}, safe=False)


def delete(request, _id): 
    if request.method == 'DELETE':
        try:
            Patient.objects.filter(pk=_id).delete()
            return JsonResponse({'message': 'successfull deleting'}, safe=False)
        except:
            return JsonResponse({'message': 'unsuccessfull deleting'}, safe=False)
    return JsonResponse({'message': 'most use DELETE method'}, safe=False)



def update(request, _id):
    if request.method == 'PUT':
        try:
            data = loads(request.body)
            Patient.objects.filter(id=_id).update(
                name = data['name'],
                family = data['family'],
                national_code = data['national_code'],
                birthday = data['birthday'],
                gender = data['gender']
                )
            return JsonResponse({'message': 'successfull updating'}, safe=False)
        except : 
            return JsonResponse({'message': 'unsuccessfull updating'}, safe=False)

