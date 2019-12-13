from django.http           import HttpResponse, JsonResponse
from django.core           import serializers
from json                  import loads
from rest_framework        import viewsets
from clinical.models       import treatment_order
from clinical.serializers  import treatment_orderSerializer
from patient.models        import Patient
from physicing.models      import physician

class treatment_orderViewSet(viewsets.ModelViewSet):
    queryset = treatment_order.objects.all().order_by('-key')
    serializer_class = treatment_orderSerializer