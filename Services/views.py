from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from .models import Services
from .serializers import ServicesSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all().order_by('-category')
    serializer_class = ServicesSerializer
