from django.contrib import admin
from django.urls import path
from . import views


app_name = 'web'
urlpatterns = [
    path('', views.drug_list, name="list"),
    path('<str:drug_no>', views.drug_detail, name='detail'),

]