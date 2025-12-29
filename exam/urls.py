from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('examsummary',views.examsummary),
    path('examschedule',views.examschedule),
    path('examdetails',views.examdetails),
]