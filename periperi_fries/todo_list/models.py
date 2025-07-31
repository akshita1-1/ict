from django.db import models

# Create your models here.
class todo(models.Model):
    taskInput=models.CharField(max_length=100)
    startInput=models.DateField()
    endInput=models.DateField()
    