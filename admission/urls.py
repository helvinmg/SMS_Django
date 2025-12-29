from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admission/', views.admission),
    path('addadmission',views.add_admission)
]