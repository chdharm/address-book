from django.db import models
from .person import Person

class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, blank=True)


