from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from ParaClininical.models import Classtreatment_order
from ParaClininical.serializers import Classtreatment_orderSerializer

class Classtreatment_orderViewSet(viewsets.ModelViewSet):
    queryset = Classtreatment_order.objects.all().order_by('-key')
    serializer_class = Classtreatment_orderSerializer