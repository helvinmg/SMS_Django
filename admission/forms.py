from django import forms
from .models import Student
#same like model creation we are creating form using modelForm
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        #['slno','name','course','phonenum','feepaid']