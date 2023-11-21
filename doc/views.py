from django.shortcuts import render
from doc.models import Docsuggest,Doctor
from client.models import Client

# Create your views here.
def docs(request):
    docs = Doctor.objects.all()
    con={
        'docs':docs,
    }
    return render(request,'doc/alldoc.html',con)


def conc(request):
    try:
        client = Client.objects.get(user=request.user)
        docsuggests = Docsuggest.objects.filter(client=client)
    except Client.DoesNotExist:
        # Handle the case when the client is not found
        docsuggests = None

    context = {
        'docsuggests': docsuggests,
    }
    return render(request, 'doc/conclusion.html', context)

