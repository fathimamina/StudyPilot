from django.urls import path 
from . import views 

urlpatterns = [
    path('module/', views.module_input, name='module_input')
]