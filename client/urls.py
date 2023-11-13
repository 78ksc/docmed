from django.urls import path
from .views import *

urlpatterns = [
    path('login/', log, name='login'),
    path('logout/', logo, name='logout'),
    path('register/', register,name='register'),
    path('account/', account, name='account'),
    path('accountedit/', accountEdit, name='accountEdit'),
]