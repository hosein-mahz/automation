from django.db import models


SERVICES_CHOISE = [
    (1, 'laser'),
    (2, 'disk'),
    (3, 'RF'),
    (4, 'epidoroscopy'),
    (5, 'endoscopy'),
]


class Services(models.Model):
    category = models.IntegerField(choices = SERVICES_CHOISE)