from django.shortcuts import render
from .models import Student
# Create your views here.
def admission(request):
    #fetch data from db
    records=Student.objects.all()#select * from student
    return render(request, 'admission_details.html',{'students':records})
