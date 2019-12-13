from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import Operation_record
from ParaClininical.serializers import Operation_recordSerializer

class Operation_recordViewSet(viewsets.ModelViewSet):
    queryset = Operation_record.objects.all().order_by('-title')
    serializer_class = Operation_recordSerializer
