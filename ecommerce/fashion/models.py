from django.db import models

# Create your models here.
class Fashion(models.Model):

    name=models.CharField(max_length=20)
    price=models.FloatField(default=0)
    brand=models.CharField(max_length=10)

