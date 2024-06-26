from django.conf import settings
from django.conf.urls.static import static
"""docmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from doc.models import Doctor,Docsuggest
from med.models import Medicen
from client.models import Appoint,Client,DocAppoint
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib.auth.decorators import login_required


def home(request):
    docs = Doctor.objects.all()[0:4]
    meds = Medicen.objects.all()[0:4]
    try:
        client = Client.objects.get(user=request.user)
        docsuggests = Docsuggest.objects.filter(client=client)
    except:
        client = None
        docsuggests = None
 
    if request.method == 'POST':
        pname = request.POST.get('pname')
        page = request.POST.get('page')
        paddr = request.POST.get('paddr')
        dspec = request.POST.get('dspec')
        psymptom = request.POST.get('psymptom')
        emergency = request.POST.get('emergency')
        Appoint.objects.create(request_created_by=client , pacient_name = pname,pacient_age = page,pacient_addr = paddr,doctor_spec = dspec,pacient_symptom = psymptom,emergency = emergency)
        return render(request, 'docappointed.html')
        # appointment_data = {
        #     'request_created_by': request.user,
        #     'pacient_name': pname,
        #     'pacient_age': page,
        #     'pacient_addr': paddr,
        #     'doctor_spec': dspec,
        #     'pacient_symptom': psymptom,
        #     'emergency': emergency,
        # }
        # Appoint.objects.create(**appointment_data)
        # Appoint.objects.create(request_created_by=request.user , *args)

    if 'doctor' in request.GET:
        doc = request.GET.get('doctor')
        print(doc)
        docvalue = Doctor.objects.get(id = doc)
        print(docvalue)
        DocAppoint.objects.create(booker = Client.objects.get(user=request.user),doctor = docvalue).save()
        return render(request, 'docappointed.html',{'i':docvalue})

    con = {
        'docs':docs,
        'meds':meds,
        'client':client,
        'docsuggests': docsuggests,
    }
    return render(request,'home.html',con)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('', include('doc.urls')),
    path('', include('med.urls')),
    path('', include('client.urls')),



    # path('appointed/', appoint, name='appoint'),
    # path('docappoint/', docappoint, name='docappoint'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

