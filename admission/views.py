from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm
# Create your views here.
def admission(request):
    #fetch data from db
    records=Student.objects.all()#select * from student
    return render(request, 'admission_details.html',{'students':records})

def add_admission(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admission')
    else:
        form=StudentForm()
    return render(request, 'admission_form.html',{'admissionform':form})