from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import Consumable_order
from ParaClininical.serializers import Consumable_orderSerializer

class Consumable_orderViewSet(viewsets.ModelViewSet):
    queryset = Consumable_order.objects.all().order_by('-qty')
    serializer_class = Consumable_orderSerializer