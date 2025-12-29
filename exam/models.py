from django.db import models

# Create your models here.
class Examscore(models.Model):
    class Grade(models.TextChoices):
        A = "A"
        B = "B"
        C = "C"
        D = "D"
        E = "E"
        F = "Fail"
    name=models.CharField(max_length=100)
    examname=models.CharField(max_length=100,default="End Semester Exam")
    marks=models.IntegerField()
    grade=models.CharField(max_length=6, choices=Grade.choices)

    def __str__(self):
        return self.name