from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import Hoteling
from ParaClininical.serializers import HotelingSerializer

class HotelingViewSet(viewsets.ModelViewSet):
    queryset = Hoteling.objects.all().order_by('-title')
    serializer_class = HotelingSerializer