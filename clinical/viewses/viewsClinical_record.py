from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from clinical.models import Clinical_record
from clinical.serializers import Clinical_recordSerializer
from patient.models import Patient
from physicing.models import physician

class Clinical_recordViewSet(viewsets.ModelViewSet):
    queryset = Clinical_record.objects.all().order_by('-data')
    serializer_class = Clinical_recordSerializer