from django.db import models

# Create your models here.
class invt(models.Model):
    product=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    discount=models.IntegerField()