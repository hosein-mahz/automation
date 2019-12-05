from django.db import models

class physician(models.Model):
    name = models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    expert=models.CharField(max_length=100)

    class Meta:
        ordering = ('expert')

    def __str__(self):
        return self.name 
