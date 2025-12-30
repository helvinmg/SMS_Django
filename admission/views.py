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

def delete_admission(request,id):
    #first visit will be GET method
    if request.method=='GET':
        return render(request, 'delete_confirm.html')
    else:
        student=Student.objects.get(pk=id)#fetching record based on primary key
        student.delete()#deleting fetched record
        #delete from student where pk=4
        return redirect('admission')
    
def update_admission(request,id):
    print("Update admission called for id:", id)
    student=Student.objects.get(pk=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('admission')
    else:
        form=StudentForm(instance=student)
    return render(request, 'update_admission.html',{'admissionform':form})