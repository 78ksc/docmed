from django.shortcuts import render
from doc.models import Doctor

# Create your views here.
def docs(request):
    docs = Doctor.objects.all()
    con={
        'docs':docs,
    }
    return render(request,'doc/alldoc.html',con)