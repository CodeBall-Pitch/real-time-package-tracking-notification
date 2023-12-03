from django.urls import path
from .views import Homeview,PackageDetailView

app_name='tracker'


urlpatterns=[
    path('',Homeview,name='home'),
    path('package/<int:tracking_number>/',PackageDetailView, name='package'),
]