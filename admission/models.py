from django.db import models

# Create your models here.
class Student(models.Model):
    #the table will be created with the following columns
    slno=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    phonenum=models.CharField(max_length=15)
    feepaid=models.BooleanField(default=False)
    #below built-in method is used to return string representation of the object, means readable info on admin
    def __str__(self):
        return self.name+"--"+self.course
