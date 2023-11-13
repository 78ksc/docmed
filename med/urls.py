from django.urls import path
from .views import *

urlpatterns = [
    path('med/',meds,name='meds')
]