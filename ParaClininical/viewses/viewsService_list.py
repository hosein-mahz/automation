from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import Service_list
from ParaClininical.serializers import Service_listSerializer

class Service_listViewSet(viewsets.ModelViewSet):
    queryset = Service_list.objects.all().order_by('-qty')
    serializer_class = Service_listSerializer