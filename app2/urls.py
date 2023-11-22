from app2.views import *
from django.urls import path

app_name='Seenu'
urlpatterns=[
    path('student/',student,name='student')
]