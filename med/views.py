from django.shortcuts import render
from med.models import Medicen

# Create your views here.
def meds(request):
    meds = Medicen.objects.all()
    con={
        'meds':meds,
    }
    return render(request,'med/allmed.html',con)