from django.db import models

# Create your models here.
class Grocery(models.Model):
    # Sno=models.IntegerField()
    item=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.CharField(max_length=50)

  


