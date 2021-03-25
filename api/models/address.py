from django.db import models
from .person import Person

class Address(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    address = models.CharField(blank=True, null=True, max_length=100)