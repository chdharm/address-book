from django.db import models
from .person import Person

class Mobile(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    mobile = models.CharField(blank=True, null=True, max_length=50)

