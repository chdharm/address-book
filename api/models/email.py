from django.db import models
from .person import Person


class Email(models.Model):
    person = models.ForeignKey(Person, editable=False, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, max_length=70, unique=True, db_index=True)
