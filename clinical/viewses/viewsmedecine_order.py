from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from clinical.models import medecine_order
from clinical.serializers import medecine_orderSerializer
from patient.models import Patient
from physicing.models import physician

class medecine_orderViewSet(viewsets.ModelViewSet):
    queryset = medecine_order.objects.all().order_by('-qty')
    serializer_class = medecine_orderSerializer