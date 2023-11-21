from django.urls import path
from .views import *

urlpatterns = [
    path('doc/',docs,name='docs'),
    path('conc/',conc,name='conc'),
]