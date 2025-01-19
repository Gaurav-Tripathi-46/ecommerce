from django.db import models

# Create your models h
class Electronics(models.Model):
    Sid=models.IntegerField()
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    desc=models.CharField(max_length=30)


    def __str__(self):
        return f"{self.Sid},{self.name},{self.price},{self.desc}"
    

    
