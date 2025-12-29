from django.shortcuts import render
from .models import Examscore

# Create your views here.
def home(request):
    return render(request, 'home.html')

def examsummary(request):
    #assume total students
    batchcount=20
    #only those who attended exam
    totalpresent=Examscore.objects.all().count()
    #only those who passed
    passcount=Examscore.objects.filter(marks__gte=40).count()
    #select count(*) from exammarks where marks>=40
    count={'pass':passcount,'fail':totalpresent-passcount,'absent':batchcount-totalpresent}
    return render(request, 'examsummary.html',count)
    #return render(request, template_name, context)
    #context is dictionary

def examschedule(request):
    dates={'day1':
           {'sub':'AI','date':'20th June'},
           'day2':
           {'sub':'CN','date':'21th June'},
           'day3':
           {'sub':'DS','date':'22nd June'},
           'day4':
           {'sub':'C++','date':'23rd June'},
           'day5':
           {'sub':'OS','date':'24th June'}}
    return render(request, 'examschedule.html',{'dates':dates})

def examdetails(request):
    marks=Examscore.objects.all()
    #fetch from exammarks model
    return render(request, 'examdetails.html', {'records': marks})