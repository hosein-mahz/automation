from django.http import HttpResponse, JsonResponse
from django.core import serializers
from json import loads
from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('-Operation_record_id')
    serializer_class = InvoiceSerializer
