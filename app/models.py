from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    timestamp = models.DateTimeField()
