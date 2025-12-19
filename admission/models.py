from django.db import models

# Create your models here.
class Student(models.Model):
    slno=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    phonenum=models.CharField(max_length=15)
    feepaid=models.BooleanField(default=False)
