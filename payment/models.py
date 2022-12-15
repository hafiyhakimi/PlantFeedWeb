from django.db import models

from member.models import Person

class Payment(models.Model):
    class Meta:
        db_table = 'payment'
    fullname = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)