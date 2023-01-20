from lzma import MODE_NORMAL
from django.db import models

# Create your models here.
class customerTable(models.Model):
    first_name = models.CharField(max_length=200, default="Vivek")
    last_name = models.CharField(max_length=200, default='Dhakad')
    address = models.CharField(max_length=200, default="NIL")
    mobile = models.BigIntegerField(default="0000000000")
    amount = models.FloatField(default="00.00")
    customerCardNumber = models.BigIntegerField(default="0000000000000000")