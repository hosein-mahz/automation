from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import patient
from json import loads


def getAll(request):
    # 
    # with database model
    # 
    g = serializers.serialize("json", patient.objects.all())
    data = loads(g)
    o = []
    for x in data:
        x['fields']['id']=x['pk']
        o = []
    return JsonResponse(data, safe=False)
