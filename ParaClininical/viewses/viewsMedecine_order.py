from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import Medecine_order
from ParaClininical.serializers import Medecine_orderSerializer

class Medecine_orderViewSet(viewsets.ModelViewSet):
    queryset = Medecine_order.objects.all().order_by('-dose')
    serializer_class = Medecine_orderSerializer