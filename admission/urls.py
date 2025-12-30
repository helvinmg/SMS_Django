from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.admission,name='admission'),
    path('addadmission',views.add_admission),
    path('delete/<int:id>/',views.delete_admission,name='delete'),
    path('update/<int:id>/',views.update_admission,name='update')
]