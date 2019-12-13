from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from physicing.models import physician
from rest_framework import viewsets
from physicing.serializers import physicianSerializer

class physicingViewSet(viewsets.ModelViewSet):
    queryset = physician.objects.all().order_by('-name')
    serializer_class = physicianSerializer