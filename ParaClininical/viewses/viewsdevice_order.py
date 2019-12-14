from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import device_order
from ParaClininical.serializers import device_orderSerializer

class device_orderViewSet(viewsets.ModelViewSet):
    queryset = device_order.objects.all().order_by('-title')
    serializer_class = device_orderSerializer