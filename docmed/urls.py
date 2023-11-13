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
from doc.models import Doctor
from med.models import Medicen
from client.models import Appoint,Client
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.contrib.auth.decorators import login_required


def home(request):
    docs = Doctor.objects.all()[0:4]
    meds = Medicen.objects.all()[0:4]
    try:
        client = Client.objects.get(user=request.user)
    except:
        client = None

    if request.method == 'POST':
        pname = request.POST.get('pname')
        page = request.POST.get('page')
        paddr = request.POST.get('paddr')
        dspec = request.POST.get('dspec')
        psymptom = request.POST.get('psymptom')
        emergency = request.POST.get('emergency')
        Appoint.objects.create(request_created_by=request.user , pacient_name = pname,pacient_age = page,pacient_addr = paddr,doctor_spec = dspec,pacient_symptom = psymptom,emergency = emergency)

    con = {
        'docs':docs,
        'meds':meds,
        'client':client,
    }
    return render(request,'home.html',con)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('', include('doc.urls')),
    path('', include('med.urls')),
    path('', include('client.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

