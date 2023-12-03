from django.urls import path
from .views import Homeview

app_name='tracker'


urlpatterns=[
    path('',Homeview,name='home')
]