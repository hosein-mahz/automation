from django.contrib import admin
from django.urls import path
from patient import views as views_patient
urlpatterns = [
    path('admin/', admin.site.urls),


    # 
    # 
    #  patient
    # 
    # 

    path('patient', views_patient.getall),
]
